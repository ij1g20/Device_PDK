# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:14:29 2025

@author: isaac
"""

import nazca as nd

with nd.Cell(name='LPCVD_CBand_TM_crossing') as LPCVD_CBand_TM_crossing:
      #load GDS BB
    cross = nd.load_gds(
        filename='LPCVD_CBand_TM_crossing.gds',
        cellname='TOP'
        )
    cross.put(0)
    nd.Pin('a0', width=1).put(-7.937, 0.057, 180)
    nd.Pin('a1', width=1).put(-0.029, 7.864, 90)
    nd.Pin('b0', width=1).put(7.937, 0.057, 0)
    nd.Pin('b1', width=1).put(-0.029, -7.864, 270)
