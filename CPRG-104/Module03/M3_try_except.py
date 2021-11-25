# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 15:57:44 2021

"""

def exception_method(a):
    try:
        return 10/a
    except ZeroDivisionError:
        print("cannot divide by 0")
        return 0
    except:
        print("Some other error occured")
        return None
        
print(exception_method(10))
print(exception_method(0))
print(exception_method(""))
