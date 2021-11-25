# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:42:23 2021

"""

class A:
    def do_something(self):
        print("Executing in A")

class B():
    def do_something(self):
        print("Executing in B")

class C(A,B):
    pass

c = C()
c.do_something()
for i in C.__mro__:
    print(i)
