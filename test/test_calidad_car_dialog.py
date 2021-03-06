# coding=utf-8
"""Dialog test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'David Castelblanco B.'
__date__ = '2017-07-24'
__copyright__ = 'Copyright 2017, cbdavide'

import unittest

from PyQt4.QtGui import QDialogButtonBox, QDialog
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt

# from calidad_car_dialog import CalidadCARDialog
from calidad_car_dialog import Ui_Dialog as CalidadCARDialog

from utilities import get_qgis_app
QGIS_APP = get_qgis_app()


class CalidadCARDialogTest(unittest.TestCase):
    """Test dialog works."""

    def setUp(self):
        """Runs before each test."""
        self.dialog = CalidadCARDialog(None)

    def tearDown(self):
        """Runs after each test."""
        self.dialog = None

    def test_dialog_ok(self):
        """Test we can click OK."""

        button = self.dialog.botonCancelar.button(QDialogButtonBox.Ok)
        button.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.Accepted)

    def test_dialog_cancel(self):
        """Test we can click cancel."""
        button = self.dialog.botonCancelar.button(QDialogButtonBox.Cancel)
        button.click()
        result = self.dialog.result()
        self.assertEqual(result, QDialog.Rejected)

    def test001_getFilePaths(self):
        """Test the the return layers of the method getFilePaths"""

        data = [('/home/shape/file.shp','fondo'),
                ('/home/shape/file.shp','hidrografia'),
                ('/home/shape/file.shp','ejes'),
                ('/home/shape/file.shp','secciones')]

        QTest.keyClicks(self.dialog.capaFondo, "/home/shape/file.shp")
        QTest.keyClicks(self.dialog.capaHidrografia, "/home/shape/file.shp")
        QTest.keyClicks(self.dialog.capaEjes, "/home/shape/file.shp")
        QTest.keyClicks(self.dialog.capaSecciones, "/home/shape/file.shp")

        result = self.dialog.getFilePaths()
        self.assertEqual(result, data)

    def test002_getFilePaths(self):
        """Test the the return layers of the method getFilePaths with 2 paths"""

        data = [('/home/shape/file.shp','fondo'),
                ('/home/shape/file.shp','secciones')]

        QTest.keyClicks(self.dialog.capaFondo, "/home/shape/file.shp")
        QTest.keyClicks(self.dialog.capaSecciones, "/home/shape/file.shp")

        result = self.dialog.getFilePaths()
        self.assertEqual(result, data)

if __name__ == "__main__":
    suite = unittest.makeSuite(CalidadCARDialogTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
