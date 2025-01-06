# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:11:09 2025

@author: ij1g20
"""

import nazca as nd
import PECVD_CBand_TE_1x3_MMI as MMI
import nazca.mask_elements as ele

mmi=MMI.PECVD_CBand_TE_1x3_MMI().put();

WG=ele.strt(10,1);

WG.put(mmi.pin['a0']);

WG.put(mmi.pin['b0']);
WG.put(mmi.pin['b1']);
WG.put(mmi.pin['b2']);


nd.export_gds(filename='PECVD_CBand_TE_1x3_MMI_example.gds')