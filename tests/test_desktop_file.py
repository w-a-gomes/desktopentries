#!/usr/bin/env python3
# python3 -m unittest discover
# python3 -m unittest
# python3 -m unittest tests.test_local_conf_dir
#
# coverage run -m unittest discover && coverage report -m
import unittest

import src.desktopentries as deskentry


class TestDesktopFile(unittest.TestCase):

    def setUp(self) -> None:
        self.desk_locate = deskentry.DesktopFilesLocation()
        self.all_desktop_file = [
            deskentry.DesktopFile(x) for x in
            self.desk_locate.desktop_files_ulrs]

    def test_if_files_is_not_none(self) -> None:
        deskfile = deskentry.DesktopFile(
            self.desk_locate.desktop_files_ulrs[0])
        self.assertIsNotNone(deskfile.desktop_file_url)
        self.assertIsNotNone(deskfile.desktop_file_as_dict)


if __name__ == '__main__':
    # No third-party testing coverage
    unittest.main()  # pragma: no cover
