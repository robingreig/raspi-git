# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 15:17:30 2021

"""

def compile_error_func():
    a = 10
    print(a)

def runtime_error_func(a):
    print(a)
    runtime_error_func(a+1)
    

compile_error_func()
runtime_error_func(5)