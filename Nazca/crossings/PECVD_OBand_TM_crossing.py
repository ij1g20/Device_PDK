# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:14:29 2025

@author: isaac
"""

import nazca as nd

with nd.Cell(name='PECVD_OBand_TM_crossing') as PECVD_OBand_TM_crossing:
      #load GDS BB
    cross = nd.load_gds(
        filename='PECVD_OBand_TM_crossing.gds',
        cellname='TOP'
        )
    cross.put(0)
    nd.Pin('a0', width=1).put(-8.595, -0.299, 180)
    nd.Pin('a1', width=1).put(0.187, 8.506, 90)
    nd.Pin('b0', width=1).put(8.595, -0.299, 0)
    nd.Pin('b1', width=1).put(0.187, -8.506, 270)
