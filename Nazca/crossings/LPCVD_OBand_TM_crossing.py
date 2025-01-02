# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:14:29 2025

@author: isaac
"""

import nazca as nd

with nd.Cell(name='LPCVD_OBand_TM_crossing') as LPCVD_OBand_TM_crossing:
      #load GDS BB
    cross = nd.load_gds(
        filename='LPCVD_OBand_TM_crossing.gds',
        cellname='TOP'
        )
    cross.put(0)
    nd.Pin('a0', width=1).put(-8.845, 0.012, 180)
    nd.Pin('a1', width=1).put(-0.172, 8.806, 90)
    nd.Pin('b0', width=1).put(8.844, 0.012, 0)
    nd.Pin('b1', width=1).put(-0.172, -8.805, 270)
