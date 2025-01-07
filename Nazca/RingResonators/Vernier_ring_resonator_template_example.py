# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 17:20:49 2025

@author: ij1g20
"""

import nazca as nd
import Vernier_ring_resonator_template as RR
import nazca.mask_elements as ele

#parameters
cell_name="C-Band Vernier Ring Resonator"
waveguide_length=100;
waveguide_width=1;
gap=0.1;
radius=60;
radius2=80;

rr=RR.Vernier_ring_resonator_template(cell_name, waveguide_length, waveguide_width, gap, radius,radius2).put();
WG=ele.strt(10,1);
WG.put(rr.pin['a0']);
WG.put(rr.pin['b0']);
WG.put(rr.pin['b1']);
WG.put(rr.pin['b2']);
WG.put(rr.pin['b3']);
WG.put(rr.pin['b4']);

nd.export_gds(filename='Vernier_ring_resonator_template_example.gds')