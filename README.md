# htimage

This library has no dependencies in the form of other libraries. It works using only the built-in Python libraries and the browser installed on your system.

The following operating systems and browsers are currently supported:

|          | MacOS | Windows | Linux |
|----------|-------|---------|-------|
| Chrome   | ✅     | ✅       | ✅     |
| Chromium | ✅     | ✅       | ✅     |
| Edge     | ✅     | ✅       | ✅     |
| Opera    | ✅     | ✅       | ✅     |

## Installation

### From GitHub

Run the following command:

```bash
pip install git+https://github.com/ArtoriasCode/htimage.git
```

## Examples

Get an image from the file:

```Python
from htimage import Htimage, Browsers


def main() -> None:
    hti = Htimage(
        browser=Browsers.CHROME
    )
    
    hti.from_file(
        file="D:/index.html",
        output="D:/image.png",
        size=(1920, 1080)
    )

if __name__ == '__main__':
    main()
```

Get an image from the link:

```Python
from htimage import Htimage, Browsers


def main() -> None:
    hti = Htimage(
        browser=Browsers.CHROME
    )
    
    hti.from_url(
        url="https://github.com/ArtoriasCode",
        output="D:/image.png",
        size=(1920, 1080)
    )

if __name__ == '__main__':
    main()
```
