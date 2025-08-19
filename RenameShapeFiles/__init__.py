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
def classFactory(iface):
    from .tool import Base
    return Base(iface)
