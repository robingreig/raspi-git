# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 15:57:44 2021

"""

def exception_method(a):
    result = None
    try:
        result = 10/a
    except ZeroDivisionError:
        print("cannot divide by 0")
        result = 0
    except:
        print("Some other error occured")
    finally:
        print("Operation Completes")
    return result
        
print(exception_method(10))
print(exception_method(0))
