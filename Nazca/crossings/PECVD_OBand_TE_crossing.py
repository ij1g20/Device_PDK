# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:14:29 2025

@author: isaac
"""

import nazca as nd

with nd.Cell(name='PECVD_OBand_TE_crossing') as PECVD_OBand_TE_crossing:
      #load GDS BB
    cross = nd.load_gds(
        filename='PECVD_OBand_TE_crossing.gds',
        cellname='TOP'
        )
    cross.put(0)
    nd.Pin('a0', width=1).put(-8.579, -0.194, 180)
    nd.Pin('a1', width=1).put(0.177, 8.495, 90)
    nd.Pin('b0', width=1).put(8.578, -0.194, 0)
    nd.Pin('b1', width=1).put(0.177, -8.495, 270)
