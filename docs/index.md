# desktopentryparse
[https://github.com/w-a-gomes/desktopentryparse](https://github.com/w-a-gomes/desktopentryparse)

Python lib to find and provide easy access to desktop files values.

Follows the specification from freedesktop.org: www.freedesktop.org/wiki/Specifications/basedir-spec/

No dependencies, just use the standard library.

### Sample
```python
>>> desktop_file = DesktopFile(url='/usr/share/applications/firefox.desktop')
>>> desktop_file.as_dict['[Desktop Entry]']['Name']
'Firefox Web Browser'
```