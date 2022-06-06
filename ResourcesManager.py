# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:09:44 2022

@author: nghia_sv
"""

import SPEC_DEFAULT as SPEC
from SlotMachine import *
from Symbol import *

def dig(structure, func):
    struct_type = type(structure)
    output = None
    if struct_type == list:
        output = []
        for item in structure:
            output.append(func(item))
        
        return output
    
    elif struct_type == dict:
        output = dict()
        for key in structure:
            value = structure[key]
            output[key] = dig(value, func)
        
        return output
    
    else:
        return func(structure)
        

class ResourcesManager:
    def __init__(self, load_func, resources_files=SPEC.RESOURCES_FILES):
        self.resources_files = resources_files
        self.resources = dig(self.resources_files, load_func)
    
    def lookup(self, obj_type):
        if   obj_type == SlotMachine:
            return self.resources[SPEC._RES_KEY_SLOT_MACHINE]
        elif obj_type == SymbolCricket:
            return self.resources[SPEC._RES_KEY_SYMBOL_CRICKET]
        else:
            return None