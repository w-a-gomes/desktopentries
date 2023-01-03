#!/usr/bin/env python3
# python3 -m unittest discover
# python3 -m unittest
# python3 -m unittest tests.test_local_conf_dir
#
# coverage run -m unittest discover && coverage report -m && coverage html
import os
import unittest

import src.desktopentryparse as deskentry


class TestDesktopFile(unittest.TestCase):
    def setUp(self) -> None:
        self.xdg_data_home_initial_value = True
        if not os.environ.get('XDG_DATA_HOME'):
            self.xdg_data_home_initial_value = False
            os.environ['XDG_DATA_HOME'] = os.path.join(
                os.environ['HOME'], '.local', 'share')

        self.desk_locate = deskentry.FileLocations()
        self.all_desktop_file = [
            deskentry.DesktopFile(x) for x in
            self.desk_locate.files_ulr_by_priority]

    def tearDown(self) -> None:
        if not self.xdg_data_home_initial_value:
            os.environ.pop('XDG_DATA_HOME', None)

    def test_if_files_is_not_none(self) -> None:
        deskfile = deskentry.DesktopFile(
            self.desk_locate.files_ulr_by_priority[0])
        self.assertIsNotNone(deskfile.url)
        self.assertIsNotNone(deskfile.content)

    def test_desktop_file_dict(self) -> None:
        for i in self.all_desktop_file:
            self.assertIn('[Desktop Entry]', i.content)
            self.assertIn('Name', i.content['[Desktop Entry]'])
            self.assertIn('applications', i.url)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
