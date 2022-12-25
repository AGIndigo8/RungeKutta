"""
Author: August Garibay
Feb 2022
License: MIT

RK class implements Runge-Kutta ODE numerical algorithm. It provides interface methods evaluate and plot to easily access solutions. In general, RK can be treated as an iterable container over the points.
RK takes an arbitrary function F(x,y) where x and y are floats and the return of F is also a float. It also requires initial conditions x0 and y0. Stepsize h is used for calculations, but elements are only provided for steps of size fid (fidelity)

ATTN Dr.Benoit: For the implementation of the Runge-Kutta algorithm please see RK.step method
"""
import matplotlib.pyplot as plt

class RK:
    x0 = 0
    y0 = .1
    h = .1

    fid = 1
    x = 50
    current = (x0,y0)

    #y0 is being repurposed to be a vector of initilal values
    #F will need to be in the form F(x,y) where y is a vector of values
    def __init__(self, F, x0, y0, h):
        self.x0 = x0
        self.y0 = y0
        current = (x0,y0)
        self.h = h
        self.F = F
    
    def evaluate(self, x):
        self.fid = x
        self.x = x
        for p in self:
            return p
    
    def __iter__(self):
        self.current  = (self.x0, self.y0)
        return self

    def step(self):
        x = self.current[0]
        y = self.current[1]
        h = self.h
        F = self.F
        k1 = F(x,y)
        delta_y =[yi + ((h/2)*k1i) for yi, k1i in zip(y , k1)]
        k2 = F(x+(h/2) , delta_y)
        delta_y =[yi + ((h/2)*k2i) for yi, k2i in zip(y , k2)]
        k3 = F(x+(h/2) , delta_y)
        delta_y =[yi + (h*k3i) for yi, k3i in zip(y , k3)]
        k4 = F(x+h , delta_y)
        delta_y = [yi + ((h/6)*(k1i + (2*k2i)+(2*k3i)+k4i)) for yi, k1i, k2i, k3i, k4i in zip(y, k1, k2, k3,k4)]
        self.current = (x+h, delta_y)


    def __next__(self):
        if self.current[0] >= self.x : raise StopIteration()
        for i in range(int(self.fid/self.h)): self.step()
        out= self.current
        return out

