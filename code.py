# --------------
import pandas as pd
import numpy as np
import math


#Code starts here
class complex_numbers():
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
       # complex(self.real,self.imag)
   
    def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))    
    def __add__(self, other):
        a=self.real + other.real
        b=self.imag + other.imag
        return complex_numbers(a,b)

    def __sub__(self, other):
        a=self.real - other.real
        b=self.imag - other.imag
        return complex_numbers(a,b)

    def __mul__(self, other):
        a=self.real*other.real - self.imag*other.imag
        b=self.imag*other.real + self.real*other.imag
        return complex_numbers(a,b)

    def __truediv__(self, other):
        sr, si, oR, oi = self.real, self.imag, other.real, other.imag 
        r = float(oR**2 + oi**2)
        return complex_numbers((sr*oR+si*oi)/r, (si*oR-sr*oi)/r)
    def absolute(self):
        a=math.sqrt(self.real**2+self.imag**2)
        return a
    def argument(self):
        a= np.angle(complex(self.real,self.imag),deg=True)
        return round(a,2)

    def conjugate(self):
        return np.conjugate(complex(self.real,self.imag))

comp_1=complex_numbers(3,5)
comp_2=complex_numbers(4,4)
comp_sum=comp_1+comp_2
comp_diff=comp_1-comp_2
comp_prod=comp_1*comp_2
comp_quot=comp_1/comp_2
comp_abs=complex_numbers.absolute(comp_1)
comp_conj=complex_numbers.conjugate(comp_1)
comp_arg=complex_numbers.argument(comp_1)


