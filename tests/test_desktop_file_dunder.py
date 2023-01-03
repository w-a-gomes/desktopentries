#!/usr/bin/env python3
import os
import unittest

import src.desktopentryparse as deskentry


class TestDesktopFileDunder(unittest.TestCase):

    def setUp(self) -> None:
        file_path = os.path.dirname(os.path.abspath(__file__))
        self.firefox = deskentry.DesktopFile(
            url=os.path.join(file_path, 'firefox.desktop'))
        self.blender = deskentry.DesktopFile(
            url=os.path.join(file_path, 'blender.desktop'))
        self.dif_ini = deskentry.DesktopFile(
            url=os.path.join(file_path, 'dif.desktop'))

    def test_gt(self) -> None:
        self.assertGreater(self.firefox, self.blender)
        self.assertGreater(self.dif_ini, self.blender)

    def test_lt(self) -> None:
        self.assertLess(self.blender, self.firefox)
        self.assertLess(self.dif_ini, self.firefox)

    def test_eq(self) -> None:
        self.assertEqual(self.blender, self.blender)
        self.assertEqual(self.dif_ini, self.dif_ini)

    def test_ge(self) -> None:
        self.assertGreaterEqual(self.firefox, self.blender)
        self.assertGreaterEqual(self.blender, self.blender)
        self.assertGreaterEqual(self.dif_ini, self.blender)
        self.assertGreaterEqual(self.dif_ini, self.dif_ini)

    def test_le(self) -> None:
        self.assertLessEqual(self.blender, self.firefox)
        # self.assertLessEqual(self.blender, self.blender)
        # self.assertLessEqual(self.ini, self.firefox)
        # self.assertLessEqual(self.ini, self.ini)

    def test_ne(self) -> None:
        self.assertNotEqual(self.blender, self.firefox)
        self.assertNotEqual(self.dif_ini, self.firefox)

    def test_str(self) -> None:
        self.assertEqual(
            '<DesktopFile: Firefox Web Browser>', str(self.firefox))
        self.assertEqual('<DesktopFile: dif>', str(self.dif_ini))
