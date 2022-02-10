"""
Author: August Garibay
Feb 2022
License: MIT

Description: Command line script for interfacing with the RK (Runge_Kutta) class. Evaluate and plot arbitrary differential equations in the for y'= F(x,y). F is provided as a python arithmatic literal and may include python math library functions such as math.sin

ATTN: Dr.Benoit. For the section of code that actually implements the Runge-Kutta algorithm, please see RK.py, RK.step(self)
"""
import sys
import math
from RK import RK

def help():
    print("Program will take a given arithmatic expression and treat it as F(x,y)=y' \n provide the expression as a python arithmatic literal of x and y exp. 10y(1-y). This parameter is called F in the folowing. F may use python math library as well exp. x*math.sin(y)")
    print("Functions:")
    print("PROGRAM_NAME.py evaluate <F> <x0> <y0> <h> <x>")
    print("  returns the Runge-Kutta with initial conditions y(x0)=y0 with stepsize h, evaluated at x.")
    print("PROGRAM_NAME.py plot <F> <x0> <y0> <h> <fidelity> <x>")
    print("  plots y(x) from Runge-Kutta at the initial conditions y(x0)=y0 with stepsize h, plotting only intervals of size fidelity up to the point x")

def build_f(F):
    definition = "def func(x,y):\n  return "
    definition = definition + F + "\nf=func"
    ldict = {}
    exec(definition, globals(), ldict)
    return ldict['f']

def build_rk(F, x0, y0, h):
    return RK(build_f(F), float(x0), float(y0), float(h))


def evaluate(rk, x):
    print(rk.evaluate(x))

def plot(rk, fid, x): 
    rk.plot('plot',float(fid),float(x))

def main():
    ops = {
        "help" : help,
        "evaluate" : evaluate,
        "plot" : plot
    }
    if(len(sys.argv) == 1): help()
    else:
        args = sys.argv[6:]
        args.insert(0,build_rk(*(sys.argv[2:6])))
        ops[sys.argv[1]](*args)


if __name__ == "__main__":
    main()
