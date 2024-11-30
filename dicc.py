import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math as m
import numpy as np

def Pol(z):
    z['r']=m.sqrt(pow(z['x'],2)+pow(z['y'],2))
    z['a']=m.atan(z['y']/z['x'])

def Rec(z):
    z['x']= z['r'] * m.cos(z['a'])
    z['y']= z['r'] * m.sin(z['a'])

def crearPol(z,r,a):
    z['r']=r
    z['a']=a*m.pi/180
    Rec(z)


def crearRec(z,x,y):
    z['x']=x
    z['y']=y
    Pol(z)

def suma(zt,z1,z2):
    zt['x']=float(z1['x']+z2['x'])
    zt['y']=float(z1['y']+z2['y'])
    Pol(zt)

def suma3(zt,z1,z2,z3):
    zt['x']=float(z1['x']+z2['x']+z3['x'])
    zt['y']=float(z1['y']+z2['y']+z3['y'])
    Pol(zt)

def producto(zt,z1,z2):
    zt['r']=float(z1['r'] * z2['r'])
    zt['a']=float(z1['a'] + z2['a'])
    Rec(zt)

def division(zt,z1,z2):
    zt['r']=float(z1['r']/z2['r'])
    zt['a']=float(z1['a']-z2['a'])
    Rec(zt)

def admitancia(y,z):
    y['r']=float(1/z['r'])
    y['a']=float(-1*z['a'])
    Rec(y)

def iniciarVoltajes():
    crearPol(urn,220,0)
    crearPol(usn,220,240)
    crearPol(utn,220,120)

def desplazamiento():
    iro=dict()
    iso=dict()
    ito=dict()
    producto(iro,yr,urn)
    producto(iso,ys,usn)
    producto(ito,yr,utn)
    numerador=dict()
    suma3(numerador,iro,iso,ito)
    denominador=dict()
    suma3(denominador,yr,ys,yt)
    division(uno,numerador,denominador)

def mostrar(z):
    if(z['x'] < 0.00000001):
        z['x'] =0
    if(z['y'] < 0.00000001):
        z['y'] =0
    if(z['r'] < 0.00000001):
        z['r'] =0
    print(f"{z['x']} ; {z['y']} <================> {z['r']} ; {z['a']*m.pi/180}")

def plot():
    ax=plt.subplot()
    ax.quiver(0,0,float(urn['x']),float(urn['y']), angles='xy',scale_units='xy', scale=1, color="red")
    ax.quiver(0,0,float(usn['x']),float(usn['y']), angles='xy',scale_units='xy', scale=1, color="blue")
    ax.quiver(0,0,float(utn['x']),float(utn['y']), angles='xy',scale_units='xy', scale=1, color="green")
    ax.quiver(0,0,float(uno['x']),float(uno['y']), angles='xy',scale_units='xy', scale=1, color="black")
    ax.set_xlim(-300,300)
    ax.set_ylim(-300,300)
    plt.xlabel("X")
    plt.xlabel("Y")
    plt.grid()
    plt.show()




urn=dict()
usn=dict()
utn=dict()
iniciarVoltajes()
print(urn)


zr=dict()
zs=dict()
zt=dict()

selectFlag=False

print("===========================INGRESO DE DATOS DE IMPEDANCIAS============================")
print("Seleccione sobre las siguientes opciones: ")
print("Opcion 1: Carga de impedancias en Polar \nOpcion 2: Carga de impedancias en Rectangular")
opcionImp=int(input("Ingrese la opcion deseada: "))
if(opcionImp == 1):
    r=float(input("Ingrese el valor del modulo de Zr: "))
    a=float(input("Ingrese el valor del argumento de Zr:"))
    print(f"los valores ingresador son: {r}, {a}")
    crearPol(zr,r,a)
    r=float(input("Ingrese el valor del modulo de Zs: "))
    a=float(input("Ingrese el valor del argumento de Zs: "))
    print(f"los valores ingresador son: {r}, {a}")
    crearPol(zs,r,a)
    r=float(input("Ingrese el valor del modulo de Zt: "))
    a=float(input("Ingrese el valor del argumento de Zt: "))
    print(f"los valores ingresador son: {r}, {a}")
    crearPol(zt,r,a)

if(opcionImp == 2):
    x=float(input("Ingrese el valor de la parte real de Zr: "))
    y=float(input("Ingrese el valor de la parte imaginaria de Zr:"))
    print(f"los valores ingresador son: {x}, {y}")
    crearRec(zr,x,y)
    x=float(input("Ingrese el valor de la parte real de Zs: "))
    y=float(input("Ingrese el valor de la parte imaginaria de Zs: "))
    print(f"los valores ingresador son: {x}, {y}")
    crearRec(zs,x,y)
    x=float(input("Ingrese el valor de la parte real de Zt: "))
    y=float(input("Ingrese el valor de la parte imaginaria de Zt: "))
    print(f"los valores ingresador son: {x}, {y}")
    crearRec(zt,x,y)

yr=dict()
ys=dict()
yt=dict()
admitancia(yr,zr)
admitancia(ys,zs)
admitancia(yt,zt)
uno=dict()
desplazamiento()
print(uno)
mostrar(uno)
plot()


#crearRec(zr,3,4)
#crearPol(z2,5,-53.13*m.pi/180)
#suma(zt,zr,z2)
#producto(zp,zr,z2)
