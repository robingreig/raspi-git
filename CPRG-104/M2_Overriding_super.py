# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:21:21 2021

"""

class A:
    def display(self):
        print("I'm in A")
    
    def show(self):
        print("Show A")
    
class B(A):
    def display(self):
        print("I'm in B")
    
    def show(self):
        A.show(self)
        super().show()
        print("Show B")
    
b = B()
b.display()
b.show()
