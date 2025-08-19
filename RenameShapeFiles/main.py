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

import os
from qgis.core import *
from qgis.utils import iface
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from PyQt5 import uic

from RenameShapeFiles.gui.diagRename import Ui_MainWindow
from RenameShapeFiles.rename.renamer import fRename

class DialogMain (QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn1.clicked.connect(self.dialogOpen)
        self.ui.btn2.clicked.connect(self.info)
        self.ui.btn3.clicked.connect(self.coffe)
        self.ui.btn4.clicked.connect(self.proceso)
        self.ui.btn5.clicked.connect(self.Close)

    def dialogOpen(self):
        opciones = QFileDialog.Options()
        carpetaEntrada = QFileDialog.getExistingDirectory(self, "Selecciona una carpeta", "/ruta/por/defecto", options=opciones)
        if not carpetaEntrada:
            return
        self.ui.line1.setText(carpetaEntrada)
        try:
            archivos_shp = [archivo for archivo in os.listdir(carpetaEntrada) if archivo.lower().endswith(".shp")]
        except OSError as e:
            iface.messageBar().pushMessage("Advertencia", "Error ", f"No se pudo leer la carpeta:\n{e}", Qgis.Warning, 3)
            return
        self.ui.cmb1.clear()
        for archivo in archivos_shp:  
            self.ui.cmb1.addItem(archivo)

    def proceso(self):
        directory = self.ui.line1.text()
        archivo = self.ui.cmb1.currentText() 
        prefix = self.ui.line2.text()
        if directory != "" and prefix != "":
            try:
                nom, ext = archivo.split(".")
                nombre = fRename.rename_files(directory, nom, prefix)
            except Exception as e:
                iface.messageBar().pushMessage("Advertencia", "error " + str(e), Qgis.Warning, 3)
        else:
            iface.messageBar().pushMessage("Advertencia", "Ingresa directorio del producto del shapefile o el prefijo.", Qgis.Warning, 3)
        
        iface.messageBar().pushMessage("Mensaje", f"Proceso concluido: archivos {nombre}", Qgis.Info, 3)
    
    def info(self):
        msgINFO = QMessageBox()
        msgINFO.setWindowIcon(QIcon(":/imgBase/img/rename0.png"))
        msgINFO.setWindowTitle("Renombrar productos de un archivo shapefile (.shp)")
        text = "<b>Renombrar archivos</b><br>" \
                "Es un complemento de QGIS para renombrar productos de un shapefile a partir de ubicar el directorio de trabajo y escribir el nuevo nombre del archivo.<br><br>" \
                "<b>Desarrollado por:</b> Héctor Solares Hernández <br><br> " \
                "<b>PyQGIS plugin developer especializado en análisis geoespacial y geoinformática."\
                "<b>Contacto:</b> hsolaresh@uaemex.mx."
        msgINFO.setText(text)
        msgINFO.setTextFormat(Qt.RichText)
        msgINFO.setStandardButtons(QMessageBox.Ok)
        msgINFO.exec_()
    
    def coffe(self):
        msgINFO = QMessageBox()
        msgINFO.setWindowIcon(QIcon(":/imgBase/img/rename1.png"))
        msgINFO.setWindowTitle("Haz que suceda: Apoyo para el desarrollo del plugins")
        text = "<b><h3>Renombrar archivos</h3></b>"\
                "Si la herramienta te ayudado ahorrado tiempo o ha hecho que tu trabajo más fácil, considera por favor en apoyarme. " \
                "Tu ayuda me permitirá seguir creando contenido útil y compartir de forma gratuita.<br><br>"\
                "<b>Muchas gracias por ser parte de esto</b><br><br>"\
                "<b>¡Juntos lo hacemos posible! 🌟</b><br><br>"\
                "<b>Cuenta:</b> 4189143295312832   Banco: BANORTE <br><br>"\
                "<b>10$😊  </b> <b>20$😊  </b> <b>50$😊</b> pesos mexicanos"
        msgINFO.setText(text)
        msgINFO.setTextFormat(Qt.RichText)
        msgINFO.setStandardButtons(QMessageBox.Ok)
        msgINFO.exec_()

    def Close(self):
        self.close()
        
