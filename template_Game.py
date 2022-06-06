# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 23:28:39 2022

@author: nghia_sv
"""

import pygame
from pygame.locals import *

_WINDOW_W = 640
_WINDOW_H = 400

class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.window_w, self.window_h = _WINDOW_W, _WINDOW_H
        self.size = (self.weight, self.height)
    
    """
    init() creates everything
    we need a separated on_init() for other tasks (future expansion)
    """
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        return True
    
    """
    event() proceeds events like pressed keys, mouse motion etc
    """
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    """
    update() computes changes in the game world like NPC's moves, player moves, AI, game score
    """
    def on_update(self):
        pass
    
    """
    render() just prints out on the screen graphic
    """
    def on_render(self):
        pass
    
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
        self.on_cleanup()
        
if __name__ == "__main__" :
    game = Game()
    game.on_execute()