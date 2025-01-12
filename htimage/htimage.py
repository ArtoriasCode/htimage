from subprocess import Popen, PIPE
from typing import Tuple, Optional

from htimage.utils.enums import Browsers
from htimage.finders import ChromeFinder


class Htimage:

    def __init__(self):
        self._command = '"{0}" {1} --timeout=5000 --window-size={2},{3} --screenshot="{4}" "{5}"'
        self._options = [
            "--headless",
            "--hide-scrollbars",
            "--disable-gpu",
            "--disable-infobars",
            "--disable-extensions",
            "--disable-blink-features=AutomationControlled"
        ]

    @staticmethod
    def _get_browser_path(browser: Browsers) -> Optional[str]:
        """
        Determines the path to the browser based on the passed value.

        Parameters:
        - browser: Browser type.

        Returns:
        - str | None: Path to the browser.
        """
        if browser == Browsers.CHROME:
            browser_path = ChromeFinder().find_browser()
        else:
            browser_path = None

        if browser_path is None:
            raise ValueError("Browser not found")

        return browser_path

    @staticmethod
    def _run_command(command: str) -> None:
        """
        Runs the command and kills the process after the first message is displayed.

        Parameters:
        - command: Command to run.

        Returns:
        - None.
        """
        with Popen(command, stdout=PIPE, stderr=PIPE, bufsize=1, universal_newlines=True) as process:
            any_message = process.stderr.readline()

            if any_message:
                process.kill()

    def from_url(
        self,
        url: str,
        output: str,
        size: Tuple[int, int],
        browser: Browsers
    ) -> None:
        """
        Makes a screenshot of a specified link.

        Parameters:
        - url: Site url.
        - output: Output file path.
        - size: Size of the screenshot.
        - browser: Browser type.

        Returns:
        - None.
        """
        command = self._command.format(
            self._get_browser_path(browser),
            " ".join(self._options),
            size[0], size[1],
            output,
            url
        )

        self._run_command(command)

    def from_file(
        self,
        file: str,
        output: str,
        size: Tuple[int, int],
        browser: Browsers
    ) -> None:
        """
        Makes a screenshot of a specified link.

        Parameters:
        - file: HTML file path.
        - output: Output file path.
        - size: Size of the screenshot.
        - browser: Browser type.

        Returns:
        - None.
        """
        command = self._command.format(
            self._get_browser_path(browser),
            " ".join(self._options),
            size[0], size[1],
            output,
            f"file:///{file}"
        )

        self._run_command(command)


