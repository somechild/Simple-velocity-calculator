import math
import time
from time import sleep
import sys
import os

print(' ')
print('for the one you want to find, put a "?"')
print ('note, these are all vectors')
print(' ')

vi = input('initial velocity')
vf = input('final velocity')
d = input('displacement')
a = input('acceleration')

#if (vi or vf or a or d) is (None or '?'):
    #def calc(vi,vf,d,a):
if vi is (None or '?'):
    vf=float(vf)
    d=float(d)
    a=float(a)
    vi = pow(vf,2) - 2*a*d
    print('vi is',vi, 'm/s')
    #return(vi)
elif vf is (None or '?'):
    vi=float(vi)
    d=float(d)
    a=float(a)
    vf = math.sqrt(pow(vi,2) + 2*a*d)
    print('vf is',vf, 'm/s')
    #return(vf)
elif d is (None or '?'):
    vf=float(vf)
    vi=float(vi)
    a=float(a)
    d = (pow(vf,2) - pow(vi,2))/(2*a)
    print('d is', d, 'm')
    #return(d)
elif a is (None or '?'):
    vf=float(vf)
    d=float(d)
    vi=float(vi)
    a= (pow(vf,2) - pow(vi,2))/(2*d)
    #return(a)
    print('a is ', a, 'm/s^2')

print(' ')
print('ending in 5 seconds')
time.sleep(5)
def restart():
    python=sys.executable
    os.execl(python, python, * sys.argv)

restart()
