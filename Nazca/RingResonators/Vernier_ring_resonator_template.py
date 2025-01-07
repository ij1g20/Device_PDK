# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:14:02 2025

@author: ij1g20
"""

import nazca as nd
import nazca.mask_elements as ele

    
def Vernier_ring_resonator_template(cell_name,waveguide_length,waveguide_width,gap,radius,radius2):
    with nd.Cell(name=cell_name) as RR:
        wg1 = ele.strt(waveguide_length+50, waveguide_width).put(-waveguide_length/2-50,0,0)
        ele.bend(radius, waveguide_width, angle=360).put(waveguide_width/2, gap + waveguide_width, 0)
        wg2 = ele.strt(waveguide_length+50, waveguide_width).put(-waveguide_length/2-50,gap*2 + radius*2 + waveguide_width*2,0)
        ele.bend(radius2, waveguide_width, angle=360).put(waveguide_length/2-100, gap*3 + radius*2 + waveguide_width*3, 0)
        wg3 = ele.strt(waveguide_length+50, waveguide_width).put(-waveguide_length/2-50,gap*4 + radius*2 + radius2*2 + waveguide_width*4,0)
            
        nd.Pin('a0', pin=wg1.pin['a0']).put()
        nd.Pin('b0', pin=wg1.pin['b0']).put()
        nd.Pin('b1', pin=wg2.pin['a0']).put()
        nd.Pin('b2', pin=wg3.pin['b0']).put()
        nd.Pin('b3', pin=wg2.pin['b0']).put()
        nd.Pin('b4', pin=wg3.pin['a0']).put()
    return RR
