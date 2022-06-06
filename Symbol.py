# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:08:06 2022

@author: nghia_sv
"""

import SPEC_DEFAULT as SPEC

class Symbol:
    #static internal
    _counter = 0
    
    #method
    def __init__(self):
        self.id = Symbol._counter
        self.rarity = SPEC._RARITY_COMMON
        self.value_base = 0
        self.spr = None
        
        Symbol._counter += 1
    
    def render(self, draw_on_top_func, base_layer=None, pos=(0,0)):
        spr_img = base_layer
        for spr in self.spr:
            if spr_img == None:
                spr_img = spr.copy()
            else:
                getattr(spr_img, draw_on_top_func)(spr, (0,0))
        
        return spr_img

#Cricket, common, 1
class SymbolCricket(Symbol):
    key = SPEC._RES_KEY_SYMBOL_CRICKET
    def __init__(self, resources_manager=None):
        super(SymbolCricket, self).__init__()
        self.rarity = SPEC._RARITY_COMMON
        self.value_base = 1
        self.spr = resources_manager.lookup(type(self))
    