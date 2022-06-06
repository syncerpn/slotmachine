# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:28:39 2022

@author: nghia_sv
"""

import pygame
from pygame.locals import *

from Player import Player
from SlotMachine import SlotMachine
from ResourcesManager import ResourcesManager
from Symbol import *
from enum import IntEnum, auto

_WINDOW_W = 176
_WINDOW_H = 136
_BLACK = (0,0,0)
_FRAMERATE = 60

class GameState(IntEnum):
    INIT = auto()
    WAIT_ACTION = auto()
    WAIT_SPIN = auto()
    WAIT_
    END = auto()

class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.window_w, self.window_h = _WINDOW_W, _WINDOW_H
        self.size = (self.window_w, self.window_h)
        
        self.state = GameState.INIT
        self.resources_manager = None
        self.slot_machine = None
        self.player = None
        
        self.scene = dict()
    
    """
    init() creates everything
    we need a separated on_init() for other tasks (future expansion)
    """
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        
        self.state = GameState.WAIT_ACTION
        self.resources_manager = ResourcesManager(load_func=pygame.image.load)
        self.slot_machine = SlotMachine(resources_manager=self.resources_manager)
        self.slot_machine.add_symbol(SymbolCricket)
        self.player = Player()
        self.clock = pygame.time.Clock()
        return True
    
    """
    event() proceeds events like pressed keys, mouse motion etc
    """
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            return
        
        if self.state == GameState.WAIT_ACTION:
            if event.type == pygame.MOUSEBUTTONDOWN:
                l,m,r = pygame.mouse.get_pressed()
                if l:
                    x,y = event.pos
                    print(x, y)
        
    """
    update() computes changes in the game world like NPC's moves, player moves, AI, game score
    """
    def on_update(self):
        self.slot_machine.spin()
        if self.state == GameState.WAIT_ACTION:
            pass
            return
        
        if self.state == GameState.WAIT_SPIN:
            pass
            return
    
    """
    render() just prints out on the screen graphic
    """
    def on_render(self):
        self._display_surf.fill(_BLACK)
        if self.state == GameState.ADD_SYMBOL:
            pass
        elif self.state == GameState.WAIT_ACTION:
            pass
        spr_slot_machine = self.slot_machine.render('blit')
        
        self._display_surf.blit(spr_slot_machine, (0,0))
        pygame.display.flip()
    
    """
    cleanup() collects garbage on leaving the game
    """
    def on_cleanup(self):
        pygame.quit()
    
    """
    execute() runs the game
    """
    def on_execute(self):
        if not self.on_init():
            self._running = False
        
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_update()
            self.on_render()
            # self.clock.tick(_FRAMERATE)
        self.on_cleanup()
        
if __name__ == '__main__':
    game = Game()
    game.on_execute()