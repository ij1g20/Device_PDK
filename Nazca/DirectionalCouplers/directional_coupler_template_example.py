# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:11:09 2025

@author: ij1g20
"""

import nazca as nd
import directional_coupler_template as DC
import nazca.mask_elements as ele

#Directional coupler Parameters
coupled_output_waveguide_length=20;
waveguide_width=1;
input_waveguide_length=30;
coupling_length=3
straight_output_waveguide_length=5;
gap=0.2;
angle_stop=15;
radius=103;

dc=DC.diretional_coupler_template(coupled_output_waveguide_length, waveguide_width, input_waveguide_length, coupling_length, straight_output_waveguide_length, gap, angle_stop, radius).put();

WG=ele.strt(10,1);

WG.put(dc.pin['a0']);
WG.put(dc.pin['b0']);
WG.put(dc.pin['b1']);

nd.export_gds(filename='directional_coupler_template example.gds')