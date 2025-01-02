# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:11:09 2025

@author: ij1g20
"""

import nazca as nd
import LPCVD_CBand_1x2_MMI as MMI
import nazca.mask_elements as ele

mmi=MMI.LPCVD_CBand_1x2_MMI().put();

WG=ele.strt(10,1);

WG.put(mmi.pin['a0']);

WG.put(mmi.pin['b0']);
WG.put(mmi.pin['b1']);


nd.export_gds(filename='LPCVD_CBand_1x2_MMI_example.gds')