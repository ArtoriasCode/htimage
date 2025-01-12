from os import path
from shutil import which
from sys import platform
from subprocess import check_output
from typing import Optional

from htimage.finders.abc import Finder


class ChromeFinder(Finder):

    def find_browser(self) -> Optional[str]:
        """
        Looks for the Chrome path in the operating system.

        Parameters:
        - None.

        Returns:
        - str | None: Path to the browser.
        """
        if platform in ["win32", "win64"]:
            return self._find_win()

        elif platform == "darwin":
            return self._find_mac()

        elif platform.startswith("linux"):
            return self._find_linux()

        else:
            return None

    def _find_mac(self) -> Optional[str]:
        """
        Looks for the Chrome path on MacOS.

        Parameters:
        - None.

        Returns:
        - str | None: Path to the browser.
        """
        default_dir = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

        if path.exists(default_dir):
            return default_dir

        name = "Google Chrome.app"

        alternative_dirs = [
            item for item
            in check_output(["mdfind", name]).decode().split("\n")
            if item.endswith(name)
        ]

        if len(alternative_dirs):
            return alternative_dirs[0] + "/Contents/MacOS/Google Chrome"

        return None

    def _find_win(self) -> Optional[str]:
        """
        Looks for the Chrome path on Windows.

        Parameters:
        - None.

        Returns:
        - str | None: Path to the browser.
        """
        import winreg

        chrome_path = None
        reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"

        for hive in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
            try:
                reg_key = winreg.OpenKey(hive, reg_path, 0, winreg.KEY_READ)
                potential_path = winreg.QueryValue(reg_key, None)
                reg_key.Close()

                if path.isfile(potential_path):
                    chrome_path = potential_path
                    break
            except OSError:
                continue
            else:
                chrome_path = None

        return chrome_path

    def _find_linux(self) -> Optional[str]:
        """
        Looks for the Chrome path on Linux.

        Parameters:
        - None.

        Returns:
        - str | None: Path to the browser.
        """
        chrome_names = [
            "google-chrome",
            "google-chrome-stable"
        ]

        for name in chrome_names:
            chrome = which(name)

            if chrome is not None:
                return chrome

        return None