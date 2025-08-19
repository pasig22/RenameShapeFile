# -*- coding: utf-8 -*-
"""
/***************************************************************************
 **Renombrar archivos shapefile .shp
 **A QGIS plugin
 **Descripcion: Renombra archivos .shp
--------------------------------------------------
        Inicio               : **agosto-2025
        copyright            : **COPYRIGHT
        email                : **keyspatial.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software: you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation, either version 1 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.core import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QAction

from .main import DialogMain


class Base:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction(
            QIcon(":/imgBase/img/rename0.png"), "Renombrar", self.iface.mainWindow()
        )
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Renombrar", self.action)

    def unload(self):
        self.iface.removePluginMenu("&Renombrar", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        self.dlg = DialogMain()
        self.dlg.show()
