# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:11:09 2025

@author: ij1g20
"""

import nazca as nd
import LPCVD_CBand_1x1_MZI as MZI
import nazca.mask_elements as ele

mzi=MZI.LPCVD_CBand_1x1_MZI(100).put();

nd.export_gds(filename='LPCVD_CBand_1x1_MZI_example.gds');