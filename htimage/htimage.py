from os import kill
from subprocess import Popen, PIPE
from typing import Tuple, List, Optional

from htimage.utils.enums import Browsers
from htimage.finders import (
    ChromeFinder,
    ChromiumFinder,
    EdgeFinder,
    OperaFinder
)


class Htimage:

    OPTIONS = [
        "--headless",
        "--hide-scrollbars",
        "--disable-gpu",
        "--disable-infobars",
        "--disable-extensions",
        "--disable-blink-features=AutomationControlled",
        "--timeout=5000"
    ]

    def __init__(self, browser: Browsers):
        self._browser_path = self._get_browser_path(browser)

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

        elif browser == Browsers.CHROMIUM:
            browser_path = ChromiumFinder().find_browser()

        elif browser == Browsers.EDGE:
            browser_path = EdgeFinder().find_browser()

        elif browser == Browsers.OPERA:
            browser_path = OperaFinder().find_browser()

        else:
            browser_path = None

        if browser_path is None:
            raise ValueError("Browser not found")

        return browser_path

    @staticmethod
    def _run_command(command: List[str], validation_text: str) -> None:
        """
        Runs the command and kills the process after the first message is displayed.

        Parameters:
        - command: Command to run.
        - validation_text: Validation text.

        Returns:
        - None.
        """
        with Popen(command, shell=False, stdout=PIPE, stderr=PIPE, bufsize=1, universal_newlines=True) as process:

            for line in process.stderr:
                if validation_text in line:
                    process.kill()

            for line in process.stdout:
                if validation_text in line:
                    process.kill()

    def _create_command(
        self,
        url: str,
        output: str,
        size: Tuple[int, int]
    ) -> List[str]:
        """
        Generates a screenshot command.

        Parameters:
        - url: Site url.
        - output: Output file path.
        - size: Size of the screenshot.

        Returns:
        - list: Command parameters.
        """
        dynamic_options = [
            self._browser_path,
            f"--window-size={size[0]},{size[1]}",
            f"--screenshot={output}",
            url
        ]

        return dynamic_options + self.OPTIONS

    def from_url(
        self,
        url: str,
        output: str,
        size: Tuple[int, int]
    ) -> None:
        """
        Makes a screenshot of a specified link.

        Parameters:
        - url: Site url.
        - output: Output file path.
        - size: Size of the screenshot.

        Returns:
        - None.
        """
        command = self._create_command(
            url=url,
            output=output,
            size=size
        )

        self._run_command(command, output)

    def from_file(
        self,
        file: str,
        output: str,
        size: Tuple[int, int]
    ) -> None:
        """
        Makes a screenshot of a specified link.

        Parameters:
        - file: HTML file path.
        - output: Output file path.
        - size: Size of the screenshot.

        Returns:
        - None.
        """
        command = self._create_command(
            url=f"file:///{file}",
            output=output,
            size=size
        )

        self._run_command(command, output)
