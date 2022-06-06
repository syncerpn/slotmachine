# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:10:01 2022

@author: nghia_sv
"""

"""
specification
"""
_RARITY_COMMON = 100
_RARITY_UNCOMMON = 50
_RARITY_RARE = 20
_RARITY_EXRARE = 5
_RARITY_LEGEND = 1

_ITEM_COIN = '_item_coin'
_ITEM_ACTIVE_SYMBOL_DESTROYER = '_item_active_symbol_destroyer'
_ITEM_ACTIVE_SYMBOL_REROLLER = '_item_active_symbol_reroller'

#slotmachine sprite
_SLOT_MACHINE_ROW = 4
_SLOT_MACHINE_COL = 5
_SLOT_MACHINE_SPR = 'resources/slotmachine.png'
_SLOT_MACHINE_SLOT_OFFSET_X = 4
_SLOT_MACHINE_SLOT_OFFSET_Y = 4
_SLOT_MACHINE_SLOT_SPACE_X = 2
_SLOT_MACHINE_SLOT_SPACE_Y = 0

#symbol
_SYMBOL_NONE_ID = -1
_SYMBOL_NONE_NAME = 'empty'

_SYMBOL_W = 32
_SYMBOL_H = 32

#symbol sprite list
_SYMBOL_NONE_SPR = 'resources/symbol_none.png'
_SYMBOL_CRICKET_SPR = 'resources/symbol_cricket.png'

"""
inference
"""
N_SYMBOL = _SLOT_MACHINE_ROW * _SLOT_MACHINE_COL

REWARD_LIST = [
    _ITEM_COIN,
    _ITEM_ACTIVE_SYMBOL_DESTROYER,
    _ITEM_ACTIVE_SYMBOL_REROLLER,
    ]

INVENTORY_LIST = [
    _ITEM_COIN,
    _ITEM_ACTIVE_SYMBOL_DESTROYER,
    _ITEM_ACTIVE_SYMBOL_REROLLER,
    ]

#resources manager
_RES_KEY_SLOT_MACHINE = 'slot_machine'

_RES_KEY_SYMBOL_CRICKET = 'symbol_cricket'

RESOURCES_FILES = {
    _RES_KEY_SLOT_MACHINE: [
        _SLOT_MACHINE_SPR,
        ],
    
    _RES_KEY_SYMBOL_CRICKET: [
        _SYMBOL_CRICKET_SPR,
        ],
    }