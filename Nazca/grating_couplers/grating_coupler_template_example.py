# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 15:32:28 2024

@author: isaac
"""
import nazca as nd
import grating_coupler_template as GC_template
import nazca.mask_elements as ele

#Grating Coupler Parameters
cell_name="PECVD O Band TE Grating Coupler"
waveguide_width=0.7;
grating_width=14;
taper_length=300
pre_grating_length=10;
post_grating_length=10;
period=0.989;
fill_factor=0.5;
number_of_gratings=30;

GC=GC_template.grating_coupler_template(cell_name, waveguide_width, grating_width, taper_length, pre_grating_length, post_grating_length, period, fill_factor, number_of_gratings);
GC.put(0,0);
waveguide=ele.strt(1000, waveguide_width).put()
GC.put('b0'); #Connects b0 of GC to the default pin of the waveguide

nd.export_gds(filename='Grating Coupler Template Example.gds')