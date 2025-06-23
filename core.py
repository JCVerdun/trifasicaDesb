import matplotlib.pyplot as plt
import math as m
from reportlab.pdfgen.canvas import Canvas
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


# ================== AUX FUNCTIONS =======================#
def crearPol(z,r,a):
    z['r'] = r
    z['a'] = a*degtor
    z['x'] = z['r'] * m.cos(z['a'])
    z['y'] = z['r'] * m.sin(z['a'])

def crearRec(z,x,y):
    z['x'] = x
    z['y'] = y
    z['r'] = m.sqrt( x**2 + y**2)
    z['a'] = m.atan2(y,x)

def suma(zt, z1, z2):
    crearRec(zt, z1['x'] + z2['x'], z1['y'] + z2['y'])


