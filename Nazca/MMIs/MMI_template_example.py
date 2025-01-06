# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:11:09 2025

@author: ij1g20
"""

import nazca as nd
import MMI_template as MMI
import nazca.mask_elements as ele

#Grating Coupler Parameters
cell_name="7x8MMI example";
number_of_inputs=7;
number_of_outputs=8;
taper_length=40;
multimode_length=100;
multimode_width=40;
taper_width=3.4;
taper_separation=1.05;
waveguide_width=1;

mmi=MMI.MMI_template(cell_name, number_of_inputs, number_of_outputs, taper_length, multimode_length, multimode_width, taper_width, taper_separation, waveguide_width).put();

WG=ele.strt(10,1);

WG.put(mmi.pin['a0']);
WG.put(mmi.pin['a1']);
WG.put(mmi.pin['a2']);
WG.put(mmi.pin['a3']);
WG.put(mmi.pin['a4']);
WG.put(mmi.pin['a5']);
WG.put(mmi.pin['a6']);

WG.put(mmi.pin['b0']);
WG.put(mmi.pin['b1']);
WG.put(mmi.pin['b2']);
WG.put(mmi.pin['b3']);
WG.put(mmi.pin['b4']);
WG.put(mmi.pin['b5']);
WG.put(mmi.pin['b6']);
WG.put(mmi.pin['b7']);



nd.export_gds(filename='MMI template example.gds')
