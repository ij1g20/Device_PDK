# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:14:29 2025

@author: isaac
"""

import nazca as nd

with nd.Cell(name='LPCVD_CBand_TE_crossing') as LPCVD_CBand_TE_crossing:
      #load GDS BB
    cross = nd.load_gds(
        filename='LPCVD_CBand_TE_crossing.gds',
        cellname='TOP'
        )
    cross.put(0)
    nd.Pin('a0', width=1).put(-8.413, -0.021, 180)
    nd.Pin('a1', width=1).put(-0.069, 8.304, 90)
    nd.Pin('b0', width=1).put(8.413, -0.021, 0)
    nd.Pin('b1', width=1).put(-0.069, -8.304, 270)
