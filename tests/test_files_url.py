#!/usr/bin/env python3
# python3 -m unittest discover
# python3 -m unittest
# python3 -m unittest tests.test_local_conf_dir
#
# coverage run -m unittest discover && coverage report -m
import os
import unittest

import src.desktopentries as deskentry


class TestFilesURL(unittest.TestCase):

    def setUp(self) -> None:
        self.desk_locate = deskentry.DesktopFilesLocation()

    def test_if_files_is_not_none(self) -> None:
        self.assertIsNotNone(self.desk_locate.desktop_file_ulrs_by_priority)
        self.assertIsNotNone(self.desk_locate.all_desktop_file_ulrs)

    def test_if_all_file_exists(self) -> None:
        for i in self.desk_locate.desktop_file_ulrs_by_priority:
            self.assertTrue(os.path.isfile(i))

        for i in self.desk_locate.all_desktop_file_ulrs:
            self.assertTrue(os.path.isfile(i))

    def test_all_file_extensions(self) -> None:
        for i in self.desk_locate.desktop_file_ulrs_by_priority:
            self.assertTrue(i.endswith('.desktop'))

        for i in self.desk_locate.all_desktop_file_ulrs:
            self.assertTrue(i.endswith('.desktop'))


if __name__ == '__main__':
    # No third-party testing coverage
    unittest.main()  # pragma: no cover
