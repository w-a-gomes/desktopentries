# desktopentryparse
https://github.com/wbin01/desktopentryparse

Python lib to find and provide easy access to desktop files values.
Follows the specification from freedesktop.org: www.freedesktop.org/wiki/Specifications/basedir-spec/

No dependencies, just use the standard library.
See the [documentation](https://wbin01.github.io/desktopentryparse) for details.

```python
>>> desktop_file = DesktopFile(url='/usr/share/applications/firefox.desktop')
>>> desktop_file.content['[Desktop Entry]']['Name']
'Firefox Web Browser'
>>> desktop_file.content['[Desktop Entry]']['Type']
'Application'
>>> for key in desktop_file.content.keys():
...     print(key)
...
...
[Desktop Entry]
[Desktop Action new - window]
[Desktop Action new - private - window]
>>>
>>> desktop_file.content['[Desktop Action new-window]']['Name']
'Open a New Window'
```
