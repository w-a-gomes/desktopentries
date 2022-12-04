#!/usr/bin/env python3
# python3 -m unittest discover
# python3 -m unittest
# python3 -m unittest tests.test_local_conf_dir
#
# coverage run -m unittest discover && coverage report -m
import os
import unittest
import src.desktopentryparse as deskentry


class TestLocation(unittest.TestCase):

    def setUp(self) -> None:
        self.desk_locate = deskentry.FileLocations()

    def test_local_conf_dir(self) -> None:
        local_conf_dir = os.path.join(
            os.environ['HOME'], '.local/share/applications')
        self.assertIn(local_conf_dir, self.desk_locate.file_dirs)

    def test_root_conf_dir(self) -> None:
        root_conf_dir = '/usr/share/applications'
        self.assertIn(root_conf_dir, self.desk_locate.file_dirs)

    def test_if_dirs_is_not_none(self) -> None:
        self.assertIsNotNone(self.desk_locate.file_dirs)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
