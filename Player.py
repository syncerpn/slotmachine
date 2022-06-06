# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:08:52 2022

@author: nghia_sv
"""

import SPEC_DEFAULT as SPEC

class Player:
    #method
    def __init__(self,
                 inventory_list=SPEC.INVENTORY_LIST):
        
        self.inventory = dict()
        for i in inventory_list:
            self.inventory[i] = 0
    
    def get_reward(self, rewards):
        for i in rewards:
            if i in self.inventory:
                self.inventory[i] += self.rewards[i]