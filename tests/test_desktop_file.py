#!/usr/bin/env python3
# python3 -m unittest discover
# python3 -m unittest
# python3 -m unittest tests.test_local_conf_dir
#
# coverage run -m unittest discover && coverage report -m && coverage html
import unittest

import src.desktopentryparse as deskentry


class TestDesktopFile(unittest.TestCase):

    def setUp(self) -> None:
        self.desk_locate = deskentry.FileLocations()
        self.all_desktop_file = [
            deskentry.DesktopFile(x) for x in
            self.desk_locate.ulrs_by_priority]

    def test_if_files_is_not_none(self) -> None:
        deskfile = deskentry.DesktopFile(
            self.desk_locate.ulrs_by_priority[0])
        self.assertIsNotNone(deskfile.url)
        self.assertIsNotNone(deskfile.as_dict)

    def test_desktop_file_dict(self) -> None:
        for i in self.all_desktop_file:
            self.assertIn('[Desktop Entry]', i.as_dict)
            self.assertIn('Name', i.as_dict['[Desktop Entry]'])
            self.assertIn('applications', i.url)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
