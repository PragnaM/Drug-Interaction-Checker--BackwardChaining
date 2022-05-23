# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 16:03:46 2021

@author: Pragna M
"""

import sys
#import pyke
from pyke import knowledge_engine, krb_traceback

my_engine = knowledge_engine.engine(__file__)

my_engine.reset()     

my_engine.activate('bc_druginteractionchecker') 

    
try:
    with my_engine.prove_goal('bc_druginteractionchecker.drug_interaction($d1, $d2)') as gen: 
        for vars, var in gen:
            print("Interaction: %s %s" % (vars['d1'], vars['d2'])) 

except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
    krb_traceback.print_exc()
    sys.exit(1)

