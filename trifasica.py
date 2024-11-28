import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math as m


class Complejo:
    def __init__(self):
        self.x=0
        self.y=0
        self.r=0
        self.a=0

    def Pol(self):
        self.r= m.sqrt(pow(self.x,2)+pow(self.y,2))
        self.a= m.atan(self.y / self.x)

    def Rec(self):
        self.x = self.r * m.cos(self.a)
        self.y= self.r * m.sin(self.a) 

    def crearRec(self,x,y):
        self.x=x
        self.y=y
        self.Pol()

    def crearPol(self,r,a):
        self.r=r
        self.a=a*m.pi/180
        self.Rec()
    
    def suma(self,z1,z2):
        self.x= z1.x + z2.x
        self.y= z1.y + z2.y
        self.Pol()
    
    def resta(self,z1,z2):
        self.x= z1.x-z2.x
        self.y=z1.y-z2.y
        self.Pol()

    def producto(self,z1,z2):
        self.r= z1.r*z2.r
        self.a= z1.a+z2.a
        self.Rec()

    def division(self,z1,z2):
        self.r=z1.r/z2.r
        self.a=z1.a-z2.a
        self.Rec()
    
    def invertir(self):
        self.a= a + m.pi
        self.Rec()
    
    def admitancia(self,z):
        self.r= 1/z.r
        self.a = -1 * z.a
        self.Rec()

def desplazamiento(self): #TODO
    x=0

urn=Complejo()
utn=Complejo()
usn=Complejo()
urn.crearPol(220,0)
utn.crearPol(220,120*m.pi/180)
usn.crearPol(220,240*m.pi/180)
urs=Complejo()
utr=Complejo()
ust=Complejo()
urs.suma(urn,)
zr=Complejo()
zs=Complejo()
zt=Complejo()
print("===========================INGRESO DE DATOS DE IMPEDANCIAS============================")
print("Seleccione sobre las siguientes opciones: ")
print("Opcion 1: Carga de impedancias en Polar \nOpcion 2: Carga de impedancias en Rectangular")
opcionImp=int(input("Ingrese la opcion deseada: "))
if(opcionImp == 1):
    r=float(input("Ingrese el valor del modulo de Zr: "))
    a=float(input("Ingrese el valor del argumento de Zr:"))
    print(f"los valores ingresador son: {r}, {a}")
    zr.crearPol(r,a)
    r=float(input("Ingrese el valor del modulo de Zs: "))
    a=float(input("Ingrese el valor del argumento de Zs: "))
    print(f"los valores ingresador son: {r}, {a}")
    zs.crearPol(r,a)
    r=float(input("Ingrese el valor del modulo de Zt: "))
    a=float(input("Ingrese el valor del argumento de Zt: "))
    print(f"los valores ingresador son: {r}, {a}")
    zt.crearPol(r,a)

if(opcionImp == 2):
    x=float(input("Ingrese el valor de la parte real de Zr: "))
    y=float(input("Ingrese el valor de la parte imaginaria de Zr:"))
    print(f"los valores ingresador son: {x}, {y}")
    zr.crearRec(x,y)
    x=float(input("Ingrese el valor de la parte real de Zs: "))
    y=float(input("Ingrese el valor de la parte imaginaria de Zs: "))
    print(f"los valores ingresador son: {x}, {y}")
    zs.crearRec(x,y)
    x=float(input("Ingrese el valor de la parte real de Zt: "))
    y=float(input("Ingrese el valor de la parte imaginaria de Zt: "))
    print(f"los valores ingresador son: {x}, {y}")
    zt.crearRec(x,y)

yr=Complejo()
ys=Complejo()
yt=Complejo()

yr.admitancia(zr)
ys.admitancia(zs)
yt.admitancia(zt)

#print(f"DEBUG ADMMITANCIA {zt.x} ; {zt.y} <====> {zt.r} ; {zt.a}")
#print(f"DEBUG ADMMITANCIA {yt.x} ; {yt.y} <====> {yt.r} ; {yt.a}")





'''z1=Complejo()
z1.crearRec(3,4)
z2=Complejo()
z2.crearPol(5,53.13)
z3=Complejo()
z3.suma(z1,z2)'''
'''print(f"DEBUG Z1 REC{z1.x} ; {z1.y} <====> {z1.r} ; {z1.a}")
print(f"DEBUG Z2 POL{z2.x} ; {z2.y} <====> {z2.r} ; {z2.a}")
print(f"DEBUG SUMA{z3.x} ; {z3.y} <====> {z3.r} ; {z3.a}")'''