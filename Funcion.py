import pygame 
from pygame import gfxdraw
import numpy as np
import math
from math import sin, cos, pi
def punto(Ventana,Color,PosPunto,Grosor):
    Ventana.fill(Color,(PosPunto,(Grosor,Grosor)))
def draw_regular_polygon(surface, color, vertex_count, radius, position):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
        for i in range(n)
    ])

def Linea(Windows,Color,pIni,pFin,Grosor):
    x1 = pIni[0]
    y1 = pIni[1]
    x2 = pFin[0]
    y2 = pFin[1]
    aux = 0
    if x1 > x2 and y1 > y2:
        aux = x1
        x1 = x2 
        x2 = aux
        aux = y1 
        y1 = y2
        y2 = aux
    
    dy = y2 - y1
    dx = x2 - x1
    stepY = -1 if dy < 0 else 1
    dy = math.fabs(dy)
    stepX = -1 if dx < 0 else 1
    dx = math.fabs(dx)
    if dx > dy:
        p = 2 * dy - dx
        incE = 2* dy
        incNE = 2 * (dy-dx)
        x = x1
        y = y1
        xEnd = x2
        stepX = 1
        punto(Windows,Color,[x,y],Grosor)
        while x != xEnd:
            x += stepX
            if p < 0:
                p+= incE
            else:
                p += incNE
                y += stepY
            punto(Windows,Color,[x,y],Grosor)
    else:
        p = 2 * dx - dy
        incE = 2 * dx
        incNE = 2 * (dx - dy)
        x = x1
        y = y1
        yEnd = y2
        stepY = 1
        punto(Windows,Color,[x,y],Grosor)
        while y != yEnd:
            y += stepY
            if p < 0:
                p += incE
            else:
                p += incNE
                x += stepX
            punto(Windows,Color,[x,y],Grosor)    
            
def DibujoCirculo(Windows,Color,xc,yc,x,y,Grosor):
    punto(Windows,Color,[xc+x,yc+y],Grosor)
    punto(Windows,Color,[xc-x,yc+y],Grosor)
    punto(Windows,Color,[xc+x,yc-y],Grosor)
    punto(Windows,Color,[xc-x,yc-y],Grosor)
    punto(Windows,Color,[xc+y,yc+x],Grosor)
    punto(Windows,Color,[xc-y,yc+x],Grosor)
    punto(Windows,Color,[xc+y,yc-x],Grosor)
    punto(Windows,Color,[xc-y,yc-x],Grosor)
        
def Circulo(Windows,Color,xc,yc,r,Grosor):
    x = 0
    y = r
    d = 3 - 2 * r
    DibujoCirculo(Windows,Color, xc,yc,x,y,Grosor)
    while (y >= x):
        x = x+1
        if(d > 0):
            y = y-1
            d = d + 4 * (x - y) +10
        else:
            d = d + 4 * x + 6
        DibujoCirculo(Windows,Color,xc,yc,x,y,Grosor);
        
def Rectangulo(Windows,Color,PosIni,PosFin,Grosor):
    x0=PosIni[0]
    y0=PosIni[1]
    x1=PosFin[0]
    y1=PosFin[1]
    aux = 0
    if x0 > x1 and y0 > y1:
        aux = x0
        x0 = x1 
        x1 = aux
        aux = y0 
        y0 = y1
        y1 = aux
    elif x0 < x1 and y0 > y1:
        aux = y0 
        y0 = y1
        y1 = aux
    elif x0 > x1 and y0 < y1:
        aux = x0 
        x0 = x1
        x1 = aux
    if(Grosor==0):
        yInc=y0
        while yInc<y1:
            Linea(Windows,Color,[x0,yInc],[x1,yInc],1)
            yInc=yInc+1
    else:
        Linea(Windows,Color,[x0,y0],[x1,y0],Grosor)
        Linea(Windows,Color,[x0,y1],[x1,y1],Grosor)
        Linea(Windows,Color,[x0,y0],[x0,y1],Grosor)
        Linea(Windows,Color,[x1,y0],[x1,y1],Grosor)