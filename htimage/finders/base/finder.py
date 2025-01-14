from os import path
from shutil import which
from sys import platform
from subprocess import check_output
from typing import Optional


class BaseFinder:

    MAC_DEFAULT_DIR = None
    MAC_FILE_NAME = None
    MAC_ALTERNATIVE_PATH = None
    WIN_REG_PATH = None
    LINUX_NAMES = None

    def find_browser(self) -> Optional[str]:
        """
        Looks for the browser path in the operating system.

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
        Looks for the browser path on MacOS.

        Parameters:
        - None.

        Returns:
        - str | None: Path to the browser.
        """
        if path.exists(self.MAC_DEFAULT_DIR):
            return self.MAC_DEFAULT_DIR

        alternative_dirs = [
            item for item
            in check_output(["mdfind", self.MAC_FILE_NAME]).decode().split("\n")
            if item.endswith(self.MAC_FILE_NAME)
        ]

        if len(alternative_dirs):
            return alternative_dirs[0] + self.MAC_ALTERNATIVE_PATH

        return None

    def _find_win(self) -> Optional[str]:
        """
        Looks for the browser path on Windows.

        Parameters:
        - None.

        Returns:
        - str | None: Path to the browser.
        """
        import winreg

        chrome_path = None

        for hive in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
            try:
                reg_key = winreg.OpenKey(hive, self.WIN_REG_PATH, 0, winreg.KEY_READ)
                potential_path = winreg.QueryValue(reg_key, None).strip('"').strip('\'')
                reg_key.Close()

                if path.exists(potential_path):
                    chrome_path = potential_path
                    break
            except OSError:
                continue
            else:
                chrome_path = None

        return chrome_path

    def _find_linux(self) -> Optional[str]:
        """
        Looks for the browser path on Linux.

        Parameters:
        - None.

        Returns:
        - str | None: Path to the browser.
        """
        for name in self.LINUX_NAMES:
            chrome = which(name)

            if chrome is not None:
                return chrome

        return None