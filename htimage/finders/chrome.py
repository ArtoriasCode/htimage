from htimage.finders.base import BaseFinder


class ChromeFinder(BaseFinder):

    MAC_DEFAULT_DIR = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    MAC_FILE_NAME = "Google Chrome.app"
    MAC_ALTERNATIVE_PATH = "/Contents/MacOS/Google Chrome"
    WIN_REG_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"
    LINUX_NAMES = [
        "google-chrome",
        "google-chrome-stable"
    ]