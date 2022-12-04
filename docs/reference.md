# Class Reference

Definitions overview
```
desktopentryparse.FileLocations()
    ulrs: list
    ulrs_by_priority: list
    file_dirs: list

desktopentryparse.DesktopFile(url: str)
    as_dict: dict
    url: str
```

## FileLocations
Locate system desktop entry file paths.
Files that contain the '.desktop' extension and are used internally by
menus to find applications.

Follows the specification from freedesktop.org: www.freedesktop.org/wiki/Specifications/basedir-spec/
```python
>>> local = FileLocations()
```

### ulrs
All desktop files ulrs (/path/file.desktop)

String list of all desktop file URLs. It may contain files with the
same name in different paths. To get valid single files, use
"ulrs_by_priority" property.

```python
>>> local = desktopentryparse.FileLocations()
>>> local.ulrs
['/home/user/.local/share/applications/jetbrains-pycharm-ce.desktop',
 '/usr/local/share/applications/vim.desktop',
 '/usr/share/applications/org.inkscape.Inkscape.desktop',
 '/usr/share/applications/vlc.desktop',
 ...
 ]
```

### ulrs_by_priority
Desktop files ulrs (/path/file.desktop)

String list of all desktop file URLs in order of priority.
If there are files with the same name, then user files in "~/.local/",
will have priority over system files. Likewise, files in
"/usr/local/share" take precedence over files in "/usr/share".

```python
>>> local = FileLocations()
>>> local.ulrs_by_priority
['/home/user/.local/share/applications/jetbrains-pycharm-ce.desktop',
 '/usr/local/share/applications/vim.desktop',
 '/usr/share/applications/org.inkscape.Inkscape.desktop',
 '/usr/share/applications/vlc.desktop',
 '/usr/share/applications/python3.10.desktop',
 '/home/user/.local/share/flatpak/exports/share/applications/org.gimp.GIMP.desktop',
 '/var/lib/flatpak/exports/share/applications/com.obsproject.Studio.desktop',
 '/var/lib/snapd/desktop/applications/ohmygiraffe_ohmygiraffe.desktop',
 ...
 ]
```

### file_dirs
All desktop files path

String list of all desktop file paths on the system as per settings
in $XDG_DATA_HOME and $XDG_DATA_DIRS of the freedesktop.org spec.
```python
>>> local = FileLocations()
>>> local.file_dirs
['/home/user/.local/share/applications',
 '/usr/local/share/applications',
 '/usr/share/applications',
 '/home/user/.local/share/flatpak/exports/share/applications',
 '/var/lib/flatpak/exports/share/applications',
 '/var/lib/snapd/desktop/applications']
```

## DesktopFile
Desktop files are files with the extension '.desktop' and are used
internally by menus to find applications. This object converts these files
into a dictionary to provide easy access to their values.

```python
desktop_file = DesktopFile(url='/usr/share/applications/firefox.desktop')
```

### as_dict
Contents of a desktop file as a dictionary.
```python
>>> desktop_file = DesktopFile(url='/usr/share/applications/firefox.desktop')
>>> desktop_file.as_dict['[Desktop Entry]']['Name']
'Firefox Web Browser'
>>> desktop_file.as_dict['[Desktop Entry]']['Type']
'Application'
>>> for key in desktop_file.as_dict.keys():
...     print(key)
...
[Desktop Entry]
[Desktop Action new-window]
[Desktop Action new-private-window]
>>>
>>> desktop_file.as_dict['[Desktop Action new-window]']['Name']
'Open a New Window'
```

### url
The URL used to construct this object, like: "/path/file.desktop".

```python
>>> desktop_file = DesktopFile(url='/usr/share/applications/firefox.desktop')
>>> desktop_file.url
'/usr/share/applications/firefox.desktop'
```