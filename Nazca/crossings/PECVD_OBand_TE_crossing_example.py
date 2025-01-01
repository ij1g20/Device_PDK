# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:29:16 2025

@author: isaac
"""

import nazca as nd
import nazca.mask_elements as ele
import PECVD_OBand_TE_crossing as Cross

cross=Cross.PECVD_OBand_TE_crossing.put();
wg=ele.strt(100,0.7);
wg.put(cross.pin['a0']);
wg.put(cross.pin['a1']);
wg.put(cross.pin['b0']);
wg.put(cross.pin['b1']);


nd.export_gds(filename='PECVD_OBand_TE_crossing_example.gds');