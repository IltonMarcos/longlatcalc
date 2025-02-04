# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LongLatCalc
                                 A QGIS plugin
 LongLatCalc
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-12-11
        copyright            : (C) 2024 by Ilton
        email                : ilton@geoone.com.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LongLatCalc class from file LongLatCalc.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .LongLatCalc import LongLatCalc
    return LongLatCalc(iface)
