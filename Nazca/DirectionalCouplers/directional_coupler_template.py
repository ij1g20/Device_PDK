# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 12:43:37 2025

@author: ij1g20
"""

import nazca as nd
import nazca.mask_elements as ele


def diretional_coupler_template(coupled_output_waveguide_length,waveguide_width,input_waveguide_length,coupling_length,straight_output_waveguide_length,gap,angle_stop,radius):
     with nd.Cell('Directional coupler') as DCs:
         ele.strt(input_waveguide_length+coupling_length+straight_output_waveguide_length,waveguide_width).put()
         nd.Pin('b0',pin=nd.cp.here()).put()
         dcwg=ele.strt(coupling_length,waveguide_width).put(input_waveguide_length,-(waveguide_width+gap))
         ele.bend(radius,waveguide_width,-angle_stop).put()
         ele.bend(radius,waveguide_width,angle_stop).put()
         ele.strt(coupled_output_waveguide_length,waveguide_width).put()
         nd.Pin('b1',pin=nd.cp.here()).put()
         nd.cp.goto(0,0,180)
         nd.Pin('a0',pin=nd.cp.here()).put()
         ele.bend(radius,waveguide_width,angle_stop).put(dcwg.pin['a0'])
     return DCs
 