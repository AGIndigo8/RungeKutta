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

    def __init__(self, F, x0, y0, h):
        self.x0 = x0
        self.y0 = y0
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
        k2 = F(x+(h/2) , y + ((h/2)*k1))
        k3 = F(x+(h/2) , y + ((h/2)*k2))
        k4 = F(x+h , y + (h*k3))
        self.current = (x+h, y + ((h/6)*(k1 + (2*k2) + (2*k3) + k4)))


    def __next__(self):
        if self.current[0] >= self.x : raise StopIteration()
        for i in range(int(self.fid/self.h)): self.step()
        out= self.current
        return out

    def plot(self, title, fid, x):
        self.fid = fid
        self.x = x
        xs = [self.x0]
        ys = [self.y0]
        for value in self:
            xs.append(value[0])
            ys.append(value[1])
        plt.plot(xs,ys)
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.title(title)
        plt.show()
