#!/usr/bin/env python3
# python3 -m unittest discover
# python3 -m unittest
# python3 -m unittest tests.test_local_conf_dir
#
# coverage run -m unittest discover && coverage report -m
import os
import unittest
import subprocess

import src.desktopentryparse as deskentry


class TestFilesURL(unittest.TestCase):

    def setUp(self) -> None:
        self.xdg_data_home_initial_value = True
        if not os.environ.get('XDG_DATA_HOME'):
            self.xdg_data_home_initial_value = False
            os.environ['XDG_DATA_HOME'] = os.path.join(
                os.environ['HOME'], '.local', 'share')

        self.desk_locate = deskentry.FileLocations()

    def tearDown(self) -> None:
        if not self.xdg_data_home_initial_value:
            os.environ.pop('XDG_DATA_HOME', None)

    def test_if_files_is_not_none(self) -> None:
        self.assertIsNotNone(self.desk_locate.files_ulr_by_priority)
        self.assertIsNotNone(self.desk_locate.files_ulr)

    def test_if_all_file_exists(self) -> None:
        for i in self.desk_locate.files_ulr_by_priority:
            self.assertTrue(os.path.isfile(i))

        for i in self.desk_locate.files_ulr:
            self.assertTrue(os.path.isfile(i))

    def test_all_file_extensions(self) -> None:
        for i in self.desk_locate.files_ulr_by_priority:
            self.assertTrue(i.endswith('.desktop'))

        for i in self.desk_locate.files_ulr:
            self.assertTrue(i.endswith('.desktop'))

    def test_if_all_desktop_file_ulrs_exists(self) -> None:
        if subprocess.getoutput('which vim') == '/usr/bin/vim':
            vim_count = [
                x for x in self.desk_locate.files_ulr
                if 'vim.desktop' in x]
            self.assertEqual(len(vim_count), 2)

    def test_desktop_file_ulrs_priority(self) -> None:
        if subprocess.getoutput('which vim') == '/usr/bin/vim':
            vim_count = [
                x for x in self.desk_locate.files_ulr_by_priority
                if 'vim.desktop' in x]
            self.assertEqual(len(vim_count), 1)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
