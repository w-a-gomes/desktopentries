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
        self.xdg_data_home_initial_value = True
        if not os.environ.get('XDG_DATA_HOME'):
            self.xdg_data_home_initial_value = False
            os.environ['XDG_DATA_HOME'] = os.path.join(
                os.environ['HOME'], '.local', 'share')

        self.desk_locate = deskentry.DesktopFileLocates()

    def tearDown(self) -> None:
        if not self.xdg_data_home_initial_value:
            os.environ.pop('XDG_DATA_HOME', None)

    def test_local_conf_dir(self) -> None:
        local_conf_dir = os.path.join(
            os.environ['HOME'], '.local/share/applications')
        self.assertIn(local_conf_dir, self.desk_locate.paths)

    def test_root_conf_dir(self) -> None:
        root_conf_dir = '/usr/share/applications'
        self.assertIn(root_conf_dir, self.desk_locate.paths)

    def test_if_dirs_is_not_none(self) -> None:
        self.assertIsNotNone(self.desk_locate.paths)

    def test_if_xdg_data_dirs_is_not_set(self) -> None:
        xdg_data_dirs_bkp = os.environ.get('XDG_DATA_DIRS')
        os.environ.pop('XDG_DATA_DIRS', None)

        desk_locate = deskentry.DesktopFileLocates()

        if xdg_data_dirs_bkp:
            os.environ['XDG_DATA_DIRS'] = xdg_data_dirs_bkp

        self.assertIn('/usr/local/share/applications', desk_locate.paths)

    def test_if_xdg_data_home_is_not_set(self) -> None:
        xdg_data_home_bkp = os.environ.get('XDG_DATA_HOME')
        os.environ.pop('XDG_DATA_HOME', None)

        desk_locate = deskentry.DesktopFileLocates()

        if xdg_data_home_bkp:
            os.environ['XDG_DATA_HOME'] = xdg_data_home_bkp

        home = os.environ['HOME']
        self.assertIn(
            os.path.join(home, '.local', 'share', 'applications'),
            desk_locate.paths)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
