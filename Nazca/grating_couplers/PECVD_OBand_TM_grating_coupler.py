# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 14:47:15 2024

@author: isaac
"""
import nazca as nd 
import nazca.mask_elements as ele

def grating_coupler_template():
    #Grating coupler template based on Tam's 477_PlasmoniAC_Passive GDS
    
    #Parameters
    cell_name="PECVD O Band TM Grating Coupler"
    waveguide_width=0.7;
    grating_width=14;
    taper_length=300
    pre_grating_length=10;
    post_grating_length=10;
    period=1.095;
    fill_factor=0.56;
    number_of_gratings=80;
    
    #GDS creation code
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
