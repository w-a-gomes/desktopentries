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


if __name__ == '__main__':
    # No third-party testing coverage
    unittest.main()  # pragma: no cover
