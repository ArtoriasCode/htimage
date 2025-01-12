from htimage.finders.base import BaseFinder


class ChromiumFinder(BaseFinder):

    MAC_DEFAULT_DIR = r"/Applications/Chromium.app/Contents/MacOS/Chromium"
    MAC_FILE_NAME = "Chromium.app"
    MAC_ALTERNATIVE_PATH = "/Contents/MacOS/Chromium"
    WIN_REG_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
    LINUX_NAMES = [
        "chromium-browser",
        "chromium"
    ]