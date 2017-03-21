# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SortLayers
                                 A QGIS plugin
 Sorts layers in Layers Panel alphabetically
                             -------------------
        begin                : 2017-03-21
        copyright            : (C) 2017 by Mikhail Minin
        email                : m.minin@jacobs-university.de
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
    """Load SortLayers class from file SortLayers.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sort_layers import SortLayers
    return SortLayers(iface)
