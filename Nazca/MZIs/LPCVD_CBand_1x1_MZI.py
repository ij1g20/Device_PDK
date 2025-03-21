# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 12:43:37 2025

@author: ij1g20
"""

import nazca as nd
import nazca.mask_elements as ele
from nazca.interconnects import Interconnect
import LPCVD_CBand_1x2_MMI as MMI


def LPCVD_CBand_1x1_MZI(path_length_difference):
    cell_name="LPCVD_CBand_1x1_MZI";
    
    ic = Interconnect(width=1.0, radius=60);
    
    with nd.Cell(name=cell_name) as MZI:
        mmi1=MMI.LPCVD_CBand_1x2_MMI().put(0,0);
        
        ele.strt(20,1).put(mmi1.pin['b0']);
        ele.bend(60,1,90).put();
        ele.strt(100,1).put();
        ele.bend(60,1,-90).put();
        ele.strt(340,1).put();
        ele.bend(60,1,-90).put();
        ele.strt(100,1).put();
        ele.bend(60,1,90).put();
        top=ele.strt(20,1).put();
        
        mmi2=MMI.LPCVD_CBand_1x2_MMI().put('b1');
        
        ele.strt(20,1).put(mmi1.pin['b1']);
        ele.bend(60,1,-90).put();
        ele.strt(100+path_length_difference/2,1).put();
        ele.bend(60,1,90).put();
        ele.strt(340,1).put();
        ele.bend(60,1,90).put();
        ele.strt(100+path_length_difference/2,1).put();
        ele.bend(60,1,-90).put();
        bottom=ele.strt(20,1).put();
        
        
    return MZI