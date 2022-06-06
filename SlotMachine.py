# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:08:39 2022

@author: nghia_sv
"""

import random

from syncers_lib_print_prefix import assert_erro
import SPEC_DEFAULT as SPEC
from enum import IntEnum, auto

class SlotMachineState(IntEnum):
    IDLE = auto()
    SPIN = auto()

class SlotMachine:    
    #method
    def __init__(self,
                 n_row=SPEC._SLOT_MACHINE_ROW,
                 n_col=SPEC._SLOT_MACHINE_COL,
                 reward_list=SPEC.REWARD_LIST,
                 resources_manager=None,
                 ):
        
        self.n_row = n_row
        self.n_col = n_col
        
        #following tracks dict of actual symbols created on the way
        self.all_symbol_list = dict()
        
        #following only tracks the id
        self.symbol_list = []
        self.removed_list = []
        self.destroyed_list = []
        self.board_prev = []
        self.board = []
        self.reward_list = reward_list
        
        self.resources_manager = resources_manager
        self.spr = resources_manager.lookup(type(self))
        
    def add_symbol(self, symbol_type):
        new_symbol = symbol_type(self.resources_manager)
        self.all_symbol_list[new_symbol.id] = new_symbol
        self.symbol_list.append(new_symbol.id)
    
    def evaluate(self):
        rewards = dict()
        for i in self.reward_list:
            rewards[i] = 0
        
        return rewards
    
    def get_n_symbol(self):
        return len(self.symbol_list)
    
    def get_n_slot(self):
        return self.n_row * self.n_col
    
    def _shuffle(self):
        assert_erro(self.get_n_symbol() <= self.get_n_slot(), 'number of symbols should be smaller or equal to number of slots')
        
        symbol_list_filled = self.symbol_list + [SPEC._SYMBOL_NONE_ID] * (self.get_n_slot() - self.get_n_symbol())
        
        random.shuffle(symbol_list_filled)
        self.board = symbol_list_filled
    
    def get_slot_pos(self, slot_index):
        x = slot_index // self.n_row
        y = slot_index  % self.n_row
        return (x,y)
    
    def render(self, draw_on_top_func, base_layer=None, pos=(0,0)):
        spr_img = base_layer
        for spr in self.spr:
            if spr_img == None:
                spr_img = spr.copy()
            else:
                getattr(spr_img, draw_on_top_func)(spr, pos)
        
        for slot_index, symbol_id in enumerate(self.board):
            if symbol_id == SPEC._SYMBOL_NONE_ID:
                continue
        
            (x,y) = self.get_slot_pos(slot_index)
            symbol = self.all_symbol_list[symbol_id]
            spr_symbol_img = symbol.render(draw_on_top_func)
            
            placement_pos = (
                SPEC._SLOT_MACHINE_SLOT_OFFSET_X + x * (SPEC._SYMBOL_W + SPEC._SLOT_MACHINE_SLOT_SPACE_X),
                SPEC._SLOT_MACHINE_SLOT_OFFSET_Y + y * (SPEC._SYMBOL_H + SPEC._SLOT_MACHINE_SLOT_SPACE_Y),
                )
            getattr(spr_img, draw_on_top_func)(spr_symbol_img, placement_pos)
            
        return spr_img
    
    # def offer(self):
        
    
    def spin(self):
        """
        symbol.rarity: 100, 100, 50, 20
        symbol_x_rarity_list = 100, 200, 250, 270
        corresponding_id     =   0,   1,   2,   3
        we will sample uniformly a number 'x' in the range of (0, 270)
        if a <= x < b, choose corresponding id for the symbol
        for example, x = 120, choose id = 1
        """
        
        #reset board
        self.board_prev = self.board
        self.board = []
        
        n_slot = self.get_n_slot()
        n_symbol = self.get_n_symbol()
        
        if n_symbol < n_slot:
            self._shuffle()
            
        else:
            symbol_list_available = self.symbol_list
            
            while len(self.board) < n_slot:
                symbol_x_rarity_list = None
                for symbol_id in symbol_list_available:
                    symbol = self.all_symbol_list[symbol_id]
                    if symbol_x_rarity_list is not None:
                        symbol_x_rarity_list  = [symbol.rarity]
                    else:
                        symbol_x_rarity_list += [symbol_x_rarity_list[-1] + symbol.rarity]
                
                rarity_accum_peak = symbol_x_rarity_list[-1]
                rarity_accum_random_selected = random.randint(0, rarity_accum_peak)
                
                si = 0
                while si < len(symbol_x_rarity_list):
                    symbol_rarity = symbol_x_rarity_list[si]
                    if symbol_rarity > rarity_accum_random_selected:
                        break
                    si += 1
                
                selected_symbol_id = symbol_list_available[si]
                self.board += [selected_symbol_id]
                
                symbol_list_available = symbol_list_available[:si] + symbol_list_available[si+1:]
