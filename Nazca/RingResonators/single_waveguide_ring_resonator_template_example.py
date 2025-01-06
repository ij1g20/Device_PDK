# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:20:49 2025

@author: ij1g20
"""

import nazca as nd
import single_waveguide_ring_resonator_template as RR
import nazca.mask_elements as ele

#parameters
cell_name="C-Band Ring Resonator"
waveguide_length=100;
waveguide_width=1;
gap=0.1;
radius=60;

rr=RR.single_waveguide(cell_name, waveguide_length, waveguide_width, gap, radius).put();
WG=ele.strt(10,1);
WG.put(rr.pin['a0']);
WG.put(rr.pin['b0']);

nd.export_gds(filename='single_waveguide_ring_resonator_template_example.gds')