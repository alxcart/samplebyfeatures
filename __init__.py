# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SampleByFeature
                                 A QGIS plugin
 
This plugin calculates the sample size (n) from the population size (N), according to ISO 2859-2.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-04-14
        copyright            : (C) 2019 by Alex Santos
        email                : alxcart@gmail.com
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
    """Load SampleByFeature class from file SampleByFeature.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .samplebyfeatures import SampleByFeature
    return SampleByFeature(iface)