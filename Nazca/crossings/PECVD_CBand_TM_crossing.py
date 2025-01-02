# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:14:29 2025

@author: isaac
"""

import nazca as nd

with nd.Cell(name='PECVD_CBand_TM_crossing') as PECVD_CBand_TM_crossing:
      #load GDS BB
    cross = nd.load_gds(
        filename='PECVD_CBand_TM_crossing.gds',
        cellname='TOP'
        )
    cross.put(0)
    nd.Pin('a0', width=1).put(-8.182, 0.013, 180)
    nd.Pin('a1', width=1).put(-0.082, 8.182, 90)
    nd.Pin('b0', width=1).put(8.182, 0.013, 0)
    nd.Pin('b1', width=1).put(-0.082, -8.182, 270)
