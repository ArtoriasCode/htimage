from htimage.finders.base import BaseFinder


class EdgeFinder(BaseFinder):

    MAC_DEFAULT_DIR = r"/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
    MAC_FILE_NAME = "Microsoft Edge.app"
    MAC_ALTERNATIVE_PATH = "/Contents/MacOS/Microsoft Edge"
    WIN_REG_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\msedge.exe"
    LINUX_NAMES = [
        "microsoft-edge",
        "microsoft-edge-stable"
    ]
