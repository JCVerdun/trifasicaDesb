import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math as m


def Pol(z):
    z['r']=m.sqrt(pow(z['x'],2)+pow(z['y'],2))
    z['a']=m.atan(z['y']/z['x'])

def Rec(z):
    z['x']= z['r'] * m.cos(z['a'])
    z['y']= z['r'] * m.sin(z['a'])

def crearPol(z,r,a):
    z['r']=r
    z['a']=a
    Rec(z)


def crearRec(z,x,y):
    z['x']=x
    z['y']=y
    Pol(z)

def suma(zt,z1,z2):
    zt['x']=float(z1['x']+z2['x'])
    zt['y']=float(z1['y']+z2['y'])
    Pol(zt)

def producto(zt,z1,z2):
    zt['r']=float(z1['r'] * z2['r'])
    zt['a']=float(z1['a'] + z2['a'])
    Rec(zt)

def admitancia(y,z):
    y['r']=float(1/z['r'])
    y['a']=float(-1*z['a'])
    Rec(y)


zr=dict()
crearRec(zr,3,4)
z2=dict()
crearPol(z2,5,-53.13*m.pi/180)
zt=dict()
suma(zt,zr,z2)
zp=dict()
producto(zp,zr,z2)
