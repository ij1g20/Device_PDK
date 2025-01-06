# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 12:43:37 2025

@author: ij1g20
"""

import nazca as nd
import nazca.mask_elements as ele


def MMI_template(cell_name, number_of_inputs, number_of_outputs, taper_length, multimode_length, multimode_width, taper_width, taper_separation, waveguide_width):
       with nd.Cell(name=cell_name) as MMI:
            # input tapers
            for i in range(0, number_of_inputs):  # odd number of tapers
                taper = ele.taper(taper_length, waveguide_width, taper_width).put(0, (number_of_inputs-1-i*2)*(taper_width+taper_separation)/2, 0)
                nd.Pin('a' + str(i), pin=taper.pin['a0']).put()

            #multimode section
            ele.strt(multimode_length, multimode_width).put(taper_length+multimode_length,0,180)
            
            #output tapers
            for i in range(0, number_of_outputs): #odd number of tapers
                taper=ele.taper(taper_length,taper_width,waveguide_width).put(taper_length+multimode_length, (number_of_outputs-1-i*2)*(taper_width+taper_separation)/2, 0)
                nd.Pin('b' +str(i),pin=taper.pin['b0']).put()
            return MMI
