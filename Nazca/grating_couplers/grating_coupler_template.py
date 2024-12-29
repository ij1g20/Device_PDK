# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:47:15 2024

@author: isaac
"""
import nazca as nd
import nazca.mask_elements as ele

def grating_coupler_template(cell_name,waveguide_width,grating_width,taper_length,pre_grating_length,post_grating_length,period,fill_factor,number_of_gratings):
    #Grating coupler template based on Tam's 477_PlasmoniAC_Passive GDS
    with nd.Cell(name=cell_name) as GC:
        ele.strt(pre_grating_length, grating_width).put()
        grating_on_width=period*fill_factor;
        grating_off_width=period-grating_on_width;
        number_of_gratings-=1;
        for i in range(number_of_gratings):
            ele.strt(grating_on_width, grating_width).put(pre_grating_length+grating_on_width+i*period)
        ele.strt(post_grating_length, grating_width).put(pre_grating_length+grating_off_width+number_of_gratings*period);
        taper=ele.taper(taper_length, grating_width, waveguide_width).put();
        nd.Pin('b0',pin=nd.cp.here()).put()
        nd.put_stub();
    return GC
