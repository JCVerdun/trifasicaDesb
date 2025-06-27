import matplotlib.pyplot as plt
import math as m
import configparser
from reportlab.lib.units import cm, inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

#Registro ISOCPEUR para PDF 
pdfmetrics.registerFont(TTFont('ISOCPEUR', 'ISOCPEUR.ttf'))

#Units conversion
rtodeg = 180 /m.pi
degtor = m.pi/180

#Print formatters
modfor="{:.5f}"
degfor="{:.3f}"

#Global Variables
urn = dict()
usn = dict()
utn = dict()

urs = dict()
ust = dict()
utr = dict()

zr = dict()
zs = dict()
zt = dict()

yr = dict()
ys = dict()
yt = dict()

irn = dict()
isn = dict()
itn = dict()

iro = dict()
iso = dict()
ito = dict()

# =============== LEER CONFIG ===================== #
def leerConfig():
    config = configparser.ConfigParser()
    config.readfp(open(r'voltajes.config'))
    fase = float(config['PARAMETROS']['VOLTAJE_FASE'])
    sec = int(config['PARAMETROS']['SECUENCIA'])
    phi = float(config['PARAMETROS']['PHI_INICIAL'])
    iniciarVoltajes(fase,sec,phi)
    return sec

def iniciarVoltajes(v,op,phi):
    if(op==1):
        crearPol(urn,v,phi)
        crearPol(usn,v,(phi+240))
        crearPol(utn,v,(phi+120))
        resta(urs, urn, usn)
        resta(ust, usn, utn)
        resta(utr, utn, urn)
    elif(op==2):
        crearPol(utn,v,phi)
        crearPol(usn,v,(phi+240))
        crearPol(urn,v,(phi+120))
        resta(uts, utn, usn)
        resta(usr, usn, urn)
        resta(urt, urn, utn)
    else: 
        print("SECUENCIA INVALIDA")





# ================== AUX FUNCTIONS =======================#
def Pol(z):
    z['r']=m.sqrt(pow(z['x'],2)+pow(z['y'],2))
    z['a']=m.atan(z['y']/z['x'])
    if(z['x']< 0 and z['y']>=0):
        z['a'] -= 180 * degtor
    if(z['y']< 0 and z['a']>=0):
        z['a'] -= 180 * degtor


def Rec(z):
    z['x']= z['r'] * m.cos(z['a'])
    z['y']= z['r'] * m.sin(z['a'])

def crearPol(z,r,a):
    z['r']=r
    z['a']=a*degtor
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

def resta(zt,z1,z2):
    zt['x']=float(z1['x']-z2['x'])
    zt['y']=float(z1['y']-z2['y'])
    Pol(zt)

def admitancia(y,z):
    y['r']=float(1/z['r'])
    y['a']=float(-1*z['a'])
    Rec(y)

def suma(zt, z1, z2):
    crearRec(zt, z1['x'] + z2['x'], z1['y'] + z2['y'])


# =========== MOSTRAR PARA DEBUG =========#
def mostrar():
    print(f"{modfor.format(z['x'])} ; {modfor.format(z['y'])} ============> {modfor.format(z['r'])} ; {degfor.format(z['a']*rtodeg)}")

#================ DESPLAZAMIENTO ========#

def desplazamiento():
    numerador = dict()
    suma3(numerador, irn, isn, itn)
    denominador = dict()
    suma3(denominador, yr,ys,yt)
    division(uno, numerador, denominador)
    print('UON:::')
    mostrar(uno)
    uno['a'] -= m.pi
    Rec(uno)

# ============= CARGA DE IMPEDANCIAS POR CONSOLA ============ #

def cargarImpedancias():
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

    if(opcionImp==3):
        crearRec(zr,15,20)
        crearRec(zs,15,-15)
        crearRec(zt,25,40)
        mostrar(zr)
        mostrar(zs)
        mostrar(zt)
