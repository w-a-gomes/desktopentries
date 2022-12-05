# desktopentryparse
[https://wbin01.github.io/desktopentryparse](https://wbin01.github.io/desktopentryparse)

Python lib to find and provide easy access to desktop files values.

Follows the specification from freedesktop.org: www.freedesktop.org/wiki/Specifications/basedir-spec/

No dependencies, just use the standard library.
```python
>>> desktop_file = DesktopFile(url='/usr/share/applications/firefox.desktop')
>>> desktop_file.as_dict['[Desktop Entry]']['Name']
'Firefox Web Browser'
```