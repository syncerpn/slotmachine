# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:49:34 2022

@author: nghia_sv
"""

def assert_erro(cond, msg):
    msg = '[ ERRO ] ' + msg
    assert cond, msg

def print_erro(*args, **kwargs):
    print('[ ERRO ]', end=' ')
    print(*args, **kwargs)
    
    
def print_warn(*args, **kwargs):
    print('[ WARN ]', end=' ')
    print(*args, **kwargs)
    
    
def print_info(*args, **kwargs):
    print('[ INFO ]', end=' ')
    print(*args, **kwargs)