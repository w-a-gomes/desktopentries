#!/usr/bin/env python3
# Reference:
#   www.freedesktop.org/wiki/Specifications/
#   www.freedesktop.org/wiki/Specifications/basedir-spec/
#   www.freedesktop.org/wiki/Specifications/desktop-entry-spec/
import os
import re
from subprocess import getoutput


class DesktopFilesLocation(object):
    """Desktop files location object.

    Locate system desktop entry file paths.
    Files that contain the '.desktop' extension and are used internally by
    menus to find applications
    """
    def __init__(self) -> None:
        """Class constructor"""
        self.__desktop_file_dirs = self.__find_desktop_files()
        self.__desktop_files_ulr = None

    @property
    def desktop_file_dirs(self) -> list:
        """..."""
        return self.__desktop_file_dirs

    @property
    def desktop_files_ulr(self) -> list:
        """..."""
        if not self.__desktop_files_ulr:
            self.__desktop_files_ulr = self.__desktop_files_url_by_priority()
        return self.__desktop_files_ulr

    @staticmethod
    def __find_desktop_files() -> list:
        # Fix: XDG_DATA_DIRS not contains "$HOME/.local/share/applications"

        # XDG_DATA_DIRS not contains "$HOME/.local/share/applications".
        # Keep the default directories and check if there are more directories
        desktop_file_dirs = [
            os.path.join(os.environ['HOME'], '.local/share/applications'),
            '/usr/local/share/applications',
            '/usr/share/applications',
            os.path.join(
                os.environ['HOME'],
                '.local/share/flatpak/exports/share/applications'),
            '/var/lib/flatpak/exports/share/applications',
            '/var/lib/snapd/desktop/applications']

        for data_dir in getoutput('echo $XDG_DATA_DIRS').split(':'):
            if 'applications' in os.listdir(data_dir):

                files_dir = os.path.join(data_dir, 'applications')

                if files_dir not in desktop_file_dirs:
                    desktop_file_dirs.append(files_dir)

        return desktop_file_dirs

    def __desktop_files_url_by_priority(self) -> list:
        # get url in order of precedence

        preferred_user_path = os.path.join(
            os.environ['HOME'], '.local/share/applications')

        preferred_user_files = []
        if preferred_user_path in self.__desktop_file_dirs:
            preferred_user_files = [
                x for x in os.listdir(preferred_user_path)
                if '~' not in x and x.endswith('.desktop')]

        desktop_files = [
            os.path.join(preferred_user_path, x) for x in preferred_user_files]

        for desktop_dir in self.__desktop_file_dirs:

            if desktop_dir != preferred_user_path:
                for desktop_file in os.listdir(desktop_dir):

                    if desktop_file not in preferred_user_files:
                        if ('~' not in desktop_file
                                and desktop_file.endswith('.desktop')):
                            desktop_files.append(
                                os.path.join(desktop_dir, desktop_file))

        return desktop_files


class DesktopFile(object):
    """Desktop files object.

    Desktop files are files with the extension '.desktop' and are used
    internally by menus to find applications. This object converts these files
    into a dictionary to provide easy access to their values.
    """
    def __init__(self, desktop_file_url: str) -> None:
        """Class constructor"""
        self.__desktop_file_url = os.path.abspath(desktop_file_url)
        self.__desktop_file_as_dict = None

    @property
    def desktop_file_as_dict(self) -> dict:
        """..."""
        if not self.__desktop_file_as_dict:
            self.__set_desktop_file_as_dict()
        return self.__desktop_file_as_dict

    @property
    def desktop_file_url(self) -> str:
        """..."""
        return self.__desktop_file_url

    def __set_desktop_file_as_dict(self) -> None:
        # ...
        with open(self.__desktop_file_url, 'r') as desktop_file:
            desktop_file_line = desktop_file.read()

        desktop_scope = [
            x + y
            for x, y in zip(
                re.findall('\[[A-Z]', desktop_file_line),
                re.split('\[[A-Z]', desktop_file_line)[1:])]

        self.__desktop_file_as_dict = {}
        for scope in desktop_scope:
            escope_title = ''
            escope_keys_and_values = {}

            for index_num, scopeline in enumerate(scope.split('\n')):
                if index_num == 0:
                    escope_title = scopeline
                else:
                    if scopeline and scopeline[0] != '#' and '=' in scopeline:
                        line_key, line_value = scopeline.split('=', 1)
                        escope_keys_and_values[line_key] = line_value

            self.__desktop_file_as_dict[escope_title] = escope_keys_and_values


if __name__ == '__main__':
    desk_url = DesktopFilesLocation()
    all_desktop_file = [DesktopFile(x) for x in desk_url.desktop_files_ulr]
    for i in all_desktop_file:
        if 'Name' in i.desktop_file_as_dict['[Desktop Entry]']:
            print(i.desktop_file_as_dict['[Desktop Entry]']['Name'])
            print(i.desktop_file_url)
            print('---')
    print(len(all_desktop_file))
