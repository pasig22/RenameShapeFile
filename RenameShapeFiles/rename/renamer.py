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

class fRename:

    def rename_files(directorio, nom, prefijo): 
        os.chdir(directorio) 
        files = os.listdir() 
        for file in files:  
            if os.path.isfile(file): 
                filename, file_extension = os.path.splitext(file)
                if filename == nom:
                    new_filename = f"{prefijo}{file_extension}"
                    os.rename(file, new_filename) 
                    print(f"Renamed {file} to {new_filename}")
        return new_filename