# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:14:02 2025

@author: ij1g20
"""

import nazca as nd
import nazca.mask_elements as ele

    
def single_waveguide(cell_name,waveguide_length,waveguide_width,gap,radius):
    with nd.Cell(name=cell_name) as RR:
        wg = ele.strt(waveguide_length, waveguide_width).put(-waveguide_length/2,0,0)
        ele.bend(radius, waveguide_width, angle=360).put(waveguide_width/2, gap + waveguide_width, 0)
        wg2 = ele.strt(waveguide_length, waveguide_width).put(-waveguide_length/2,gap*2 + radius*2 + waveguide_width*2,0)
            
        nd.Pin('a0', pin=wg.pin['a0']).put()
        nd.Pin('b0', pin=wg.pin['b0']).put()
        nd.Pin('b1', pin=wg2.pin['b0']).put()
        nd.Pin('b2', pin=wg2.pin['a0']).put()
    return RR