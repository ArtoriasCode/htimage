from htimage.finders.base import BaseFinder


class OperaFinder(BaseFinder):

    MAC_DEFAULT_DIR = r"/Applications/Opera.app/Contents/MacOS/Opera"
    MAC_FILE_NAME = "Opera.app"
    MAC_ALTERNATIVE_PATH = "/Contents/MacOS/Opera"
    WIN_REG_PATH = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\opera.exe"
    LINUX_NAMES = [
        "opera",
        "opera-stable"
    ]
