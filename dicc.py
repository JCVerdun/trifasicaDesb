import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math as m
import numpy as np
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm, inch
from PIL import *
from reportlab.lib.utils import ImageReader
import configparser

'''PASAJE DE RADIAN A DEGREE'''
rtodeg= 180/m.pi
degtor= m.pi/180
'''FORMATS PARA MOSTRAR DATOS'''
degfor= "{:.3f}"
modfor="{:.5f}"


'''LEO EL ARCHIVO DE CONFIG PARA CARGA DE DATOS'''
def leerConfig():
    config = configparser.ConfigParser()
    config.readfp(open(r'voltajes.config'))
    fase = float(config['PARAMETROS']['VOLTAJE_FASE'])
    sec = int(config['PARAMETROS']['SECUENCIA'])
    phi = float(config['PARAMETROS']['PHI_INICIAL'])
    print(fase,phi,sec)
    iniciarVoltajes(fase,sec,phi)
    return sec

'''FUNCIONES AUXIXLIARES DE NUMEROS COMPLEJOS'''
def Pol(z):
    z['r']=m.sqrt(pow(z['x'],2)+pow(z['y'],2))
    z['a']=m.atan(z['y']/z['x'])

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


'''CALCULO DE VOLTAJE DE DESPLAZAMIENTO'''
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

'''FUNCION PARA MOSTRAR LOS COMPLEJOS'''
def mostrar(z):
    print(f"{modfor.format(z['x'])} ; {modfor.format(z['y'])} ========> {modfor.format(z['r'])} ; {degfor.format(z['a']*rtodeg)}")

'''PLOTEO DIAGRAMA FASORIAL'''
def plotFasorial():
    ax=plt.subplot()
    ax.quiver(0,0,float(urn['x']),float(urn['y']), angles='xy',scale_units='xy', scale=1, color="red")
    ax.quiver(0,0,float(usn['x']),float(usn['y']), angles='xy',scale_units='xy', scale=1, color="blue")
    ax.quiver(0,0,float(utn['x']),float(utn['y']), angles='xy',scale_units='xy', scale=1, color="green")
    ax.quiver(0,0,float(uno['x']),float(uno['y']), angles='xy',scale_units='xy', scale=1, color="black")
    ax.quiver(float(uno['x']),float(uno['y']),float(uro['x']),float(uro['y']),angles='xy',scale_units='xy',scale=1,color="orange")   
    ax.quiver(float(uno['x']),float(uno['y']),float(uso['x']),float(uso['y']),angles='xy',scale_units='xy',scale=1,color="lightblue")
    ax.quiver(float(uno['x']),float(uno['y']),float(uto['x']),float(uto['y']),angles='xy',scale_units='xy',scale=1,color="lightgreen")
    ax.set_xlim(-800,800)
    ax.set_ylim(-500,500)
    plt.xlabel("X")
    plt.xlabel("Y")
    ax.plot([],[],color="red",label="urn")
    ax.plot([],[],color="blue",label="usn")
    ax.plot([],[],color="green",label="utn")
    ax.plot([],[],color="black",label="uno")
    ax.plot([],[],color="orange",label="uro")
    ax.plot([],[],color="lightblue",label="uso")
    ax.plot([],[],color="lightgreen",label="uto")
    ax.legend()
    plt.grid()
    plt.savefig("fasorial.png")
    #plt.show()

'''PLOTEO DE GRAICO EN FORMA DE TRIANGULO'''
def plotTriangulo(secuencia):
    bx=plt.subplot()
    bx.clear()
    print(secuencia)
    if(secuencia == 1):
        print("SECUENCIA 1")
        '''VOLTAJES DE LINEA'''
        bx.quiver(0,0,float(urs['x']),float(urs['y']),angles='xy',scale_units='xy',scale=1,color="red")
        bx.quiver(float(urs['x']),float(urs['y']),float(ust['x']),float(ust['y']),angles='xy',scale_units='xy',scale=1,color="blue")
        bx.quiver(float(ust['x']+urs['x']),float(ust['y']+urs['y']),float(utr['x']),float(utr['y']),angles='xy',scale_units='xy',scale=1,color="green")
        
        '''VOLTAJES RESPECTO CENTRO DE ESTRELLA'''
        bx.quiver(0,0,float(uro['x']),float(uro['y']),angles='xy',scale_units='xy',scale=1,color="orange",width=0.005)
        bx.quiver(float(urs['x']),float(urs['y']),float(uso['x']),float(uso['y']),angles='xy',scale_units='xy',scale=1,color="lightblue",width=0.005)
        bx.quiver(float(ust['x']+urs['x']),float(ust['y']+urs['y']),float(uto['x']),float(uto['y']),angles='xy',scale_units='xy',scale=1,color="lightgreen",width=0.005)
        
        '''VOLTAJES DE FASE RESPECTO DEL NEUTRO'''
        bx.quiver(0,0,float(urn['x']),float(urn['y']),angles='xy',scale_units='xy',scale=1,color="grey",width=0.0035)
        bx.quiver(float(urs['x']),float(urs['y']),float(usn['x']),float(usn['y']),angles='xy',scale_units='xy',scale=1,color="grey",width=0.0035)
        bx.quiver(float(ust['x']+urs['x']),float(ust['y']+urs['y']),float(utn['x']),float(utn['y']),angles='xy',scale_units='xy',scale=1,color="grey",width=0.0035)

        bx.plot([],[],color="red",label="urn")
        bx.plot([],[],color="blue",label="usn")
        bx.plot([],[],color="green",label="utn")
        bx.plot([],[],color="black",label="uno")
        bx.plot([],[],color="orange",label="uro")
        bx.plot([],[],color="lightblue",label="uso")
        bx.plot([],[],color="lightgreen",label="uto")
        bx.legend()
    
    
    elif(secuencia==2):
        print("SECUENCIA 2")
        '''VOLTAJES DE LINEA'''
        bx.quiver(0,0,float(uts['x']),float(uts['y']),angles='xy',scale_units='xy',scale=1,color="red")
        bx.quiver(float(uts['x']),float(uts['y']),float(usr['x']),float(usr['y']),angles='xy',scale_units='xy',scale=1,color="blue")
        bx.quiver(float(usr['x']+uts['x']),float(usr['y']+uts['y']),float(urt['x']),float(urt['y']),angles='xy',scale_units='xy',scale=1,color="green")
        
        '''VOLTAJES DE FASE RESPECTO A CENTRO DE ESTRELLA'''
        bx.quiver(0,0,float(uto['x']),float(uto['y']),angles='xy',scale_units='xy',scale=1,color="orange",width=0.005)
        bx.quiver(float(usr['x']),float(usr['y']),float(uso['x']),float(uso['y']),angles='xy',scale_units='xy',scale=1,color="lightblue",width=0.005)
        bx.quiver(float(usr['x']+uts['x']),float(usr['y']+uts['y']),float(uro['x']),float(uro['y']),angles='xy',scale_units='xy',scale=1,color="lightgreen",width=0.005)
        
        '''VOLTAJES DE FASE RESPECTO A NEUTRO'''
        bx.quiver(0,0,float(utn['x']),float(utn['y']),angles='xy',scale_units='xy',scale=1,color="grey",width=0.0035)
        bx.quiver(float(usr['x']),float(usr['y']),float(usn['x']),float(usn['y']),angles='xy',scale_units='xy',scale=1,color="grey",width=0.0035)
        bx.quiver(float(usr['x']+uts['x']),float(usr['y']+uts['y']),float(utn['x']),float(utn['y']),angles='xy',scale_units='xy',scale=1,color="grey",width=0.0035)



    bx.quiver(float(urn['x']),float(urn['y']),float(uno['x']),float(uno['y']),angles='xy',scale_units='xy',scale=1,color="black")
    
    bx.set_xlim(-450,450)
    bx.set_ylim(-450,450)

    
    plt.savefig("triangulo.png")
    plt.show()

'''GENERO REPORTE PDF'''
def generarReporte():
    canvas=Canvas("Reporte.pdf")
    canvas.drawString(18,11.5 * inch,"Valores de impedancias y voltajes cargados: ")
    canvas.drawString(18,11.0*inch,f"URN= {modfor.format(urn['r'])} ; {degfor.format(urn['a']*rtodeg)}    USN= {modfor.format(usn['r'])} ; {degfor.format(usn['a']*rtodeg)}     UTN= {modfor.format(utn['r'])} ; {degfor.format(utn['a']*rtodeg)}")
    canvas.drawString(18,10.75 *inch,f"URS= {modfor.format(urs['r'])} ; {degfor.format(urs['a']*rtodeg)}    UST= {modfor.format(ust['r'])} ; {degfor.format(ust['a']*rtodeg)}     UTR= {modfor.format(utr['r'])} ; {degfor.format(utr['a']*rtodeg)}")
    canvas.drawString(18,10.5*inch,f"ZR= ({modfor.format(zr['x'])}; {modfor.format(zr['y'])}) ======> {modfor.format(zr['r'])} ; {degfor.format(zr['a']*rtodeg)}")
    canvas.drawString(18,10.25*inch,f"ZS= ({modfor.format(zs['x'])}; {modfor.format(zs['y'])}) ======> {modfor.format(zs['r'])} ; {degfor.format(zs['a']*rtodeg)}")
    canvas.drawString(18,10.0*inch,f"ZT= ({modfor.format(zt['x'])}; {modfor.format(zt['y'])}) ======> {modfor.format(zt['r'])} ; {degfor.format(zt['a']*rtodeg)}")

    im1=ImageReader("fasorial.png")
    canvas.drawImage(im1,0,72,mask="auto")
    canvas.showPage()
    im2=ImageReader("triangulo.png")
    canvas.drawImage(im2,0,72,mask="auto")
    canvas.save()

'''INICIALIZO LOS VOLTAJES SEGUN CONFIG'''
def iniciarVoltajes(v,op,phi):
    if(op == 1):
        crearPol(urn,v,phi)
        crearPol(usn,v,(phi+240))
        crearPol(utn,v,(phi+120))
        resta(urs,urn,usn)
        resta(ust,usn,utn)
        resta(utr,utn,urn)
    if(op == 2):
        crearPol(utn,v,phi)
        crearPol(usn,v,phi+240)
        crearPol(urn,v,phi+120)
        resta(uts,utn,usn)
        resta(usr,usn,urn)
        resta(urt,urn,utn)

    


    

#INICIALIZO LAS VARIABLES
urn=dict()
usn=dict()
utn=dict()
urs=dict()
ust=dict()
utr=dict()
uts=dict()
usr=dict()
urt=dict()
zr=dict()
zs=dict()
zt=dict()
#LEO CONFIG Y CARGO VALORES DE VOLTAJES DE FASE Y DE LINEA
secuencia=leerConfig()
mostrar(urs)
mostrar(ust)
mostrar(utr)

#INGRESO DE DATOS DE IMPEDANCIAS
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
    
#Obtengo las admitancias de cada impedancia 
yr=dict()
ys=dict()
yt=dict()
admitancia(yr,zr)
admitancia(ys,zs)
admitancia(yt,zt)
mostrar(yr)
mostrar(ys)
mostrar(yt)

#Inicializo voltaje de desplazamiento y lo calculo
uno=dict()
desplazamiento()


#Obtengo los voltajes de fase respecto del centro de estrella 
uro=dict()
uso=dict()
uto=dict()
suma(uro,urn,uno)
suma(uso,usn,uno)
suma(uto,utn,uno)

#Ploteo los graficos y genero el reporte correspondiente
plotFasorial()
plotTriangulo(secuencia)
generarReporte()


#crearRec(zr,3,4)
#crearPol(z2,5,-53.13*m.pi/180)
#suma(zt,zr,z2)
#producto(zp,zr,z2)
