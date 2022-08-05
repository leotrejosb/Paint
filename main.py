import pygame
import time
import numpy as np
import math
from pygame.constants import MOUSEBUTTONDOWN 
import Funcion as fun

radius = 3
draw_on = True
last_pos = (0, 0)
Black = np.array([0,0,0])
Blue = np.array([0,0,255])
Red = pygame.Color(255,0,0)
Green = pygame.Color(0,255,0)
Yellow = np.array([255,233,0])
Orange = pygame.Color(255,127,0)
Purple = pygame.Color(163,73,164)
Cian = pygame.Color(0,255,255)
Magenta = pygame.Color(255,0,255)
Gray = pygame.Color(173,173,173)
LightGrey = pygame.Color(230,230,230)
White = pygame.Color(255,255,255)
MyWindow = pygame
MyWindow.init()
paleta = pygame.image.load("lapiz.png")
line_start = None
def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0]+float(i)/distance*dx)
        y = int(start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), radius)

def SelectColor(x,y,Figure,color):
    if (x >= 0 and y >= 0 and x < 80 and y <= 24):
        fun.Rectangulo(MyWindow,Black,[0,0],[80,24],4)
        color = Black
    elif (x >= 80 and x < 160 and y >= 0 and y <= 24):
        fun.Rectangulo(MyWindow,Black,[80,0],[160,24],4)
        color = Yellow
    elif (x >= 160 and x < 240 and y >= 0 and y <= 24):
        fun.Rectangulo(MyWindow,Black,[160,0],[240,24],4)
        color = Blue
    elif (x >= 240 and x < 320 and y >= 0 and y <= 24):
        fun.Rectangulo(MyWindow,Black,[240,0],[320,24],4)
        color = Red
    elif (x >= 320 and x < 400 and y >= 0 and y <= 24):
        fun.Rectangulo(MyWindow,Black,[320,0],[400,24],4)
        color = Green
    elif (x >= 400 and x < 480 and y >= 0 and y <= 24):
        fun.Rectangulo(MyWindow,Black,[400,0],[480,24],4)
        color = Orange
    elif (x >= 480 and x < 560 and y >= 0 and y <= 24):
        fun.Rectangulo(MyWindow,Black,[480,0],[560,24],4)
        color = Purple
    elif (x >= 560 and x < 640 and y >= 0 and y <= 24):
        fun.Rectangulo(MyWindow,Black,[560,0],[640,24],4)
        color = Cian
    elif (x >= 640 and x < 720 and y >= 0 and y <= 24):
        fun.Rectangulo(MyWindow,Black,[640,0],[720,24],4)
        color = Magenta
    elif (x >= 720 and x < 800 and y >= 0 and y <= 24):
        fun.Rectangulo(MyWindow,Black,[720,0],[800,24],4)
        color = Gray
        
    return color


def SelectFigure(x,y,Figure,color):
    if (x >= 0 and x <= 72 and y >=24 and y <=96):
        fun.Rectangulo(MyWindow,Black,[0,24],[72,96],4)
        Figure = "Lapiz"
    if (x >= 0 and x <= 72 and y >=96 and y <=168):
        fun.Rectangulo(MyWindow,Black,[0,96],[72,168],4)
        Figure = "Line"
    elif (x >= 0 and x <= 72 and y >=168 and y <=240):
        fun.Rectangulo(MyWindow,Black,[0,168],[72,240],4)
        Figure = "Rect"
    elif (x >= 0 and x <= 72 and y >=240 and y <=312):
        fun.Rectangulo(MyWindow,Black,[0,240],[72,312],4)
        Figure = "RectFill"
    elif (x >= 0 and x <= 72 and y >=312 and y <=384):
        fun.Rectangulo(MyWindow,Black,[0,312],[72,384],4)
        Figure = "Cir"
    elif (x >= 0 and x <= 72 and y >=384 and y <=456):
        fun.Rectangulo(MyWindow,Black,[0,384],[72,456],4)
        Figure = "CirFill"
    elif (x >= 0 and x <= 72 and y >=456 and y <=528):
        fun.Rectangulo(MyWindow,Black,[0,456],[72,528],4)
        Figure = "Triangle"
    elif (x >= 0 and x <= 72 and y >=528 and y <=600):
        fun.Rectangulo(MyWindow,Black,[0,528],[72,600],4)
        Figure = "Penta"
    return Figure
    
def Barras(MyWindow):
    fun.Rectangulo(MyWindow,Black,[0,0],[80,24],0)
    fun.Rectangulo(MyWindow,Yellow,[80,0],[160,24],0)
    fun.Rectangulo(MyWindow,Blue,[160,0],[240,24],0)
    fun.Rectangulo(MyWindow,Red,[240,0],[320,24],0)
    fun.Rectangulo(MyWindow,Green,[320,0],[400,24],0)
    fun.Rectangulo(MyWindow,Orange,[400,0],[480,24],0)
    fun.Rectangulo(MyWindow,Purple,[480,0],[560,24],0)
    fun.Rectangulo(MyWindow,Cian,[560,0],[640,24],0)
    fun.Rectangulo(MyWindow,Magenta,[640,0],[720,24],0)
    fun.Rectangulo(MyWindow,Gray,[720,0],[800,24],0)
    fun.Rectangulo(MyWindow,LightGrey,[0,24],[72,600],0)
    fun.Linea(MyWindow,Black,[72,24],[72,600],4)
    fun.Linea(MyWindow,Black,[0,24],[800,24],4)
    fun.Rectangulo(MyWindow,Black,[0,24],[72,96],2)
    fun.Rectangulo(MyWindow,Black,[0,96],[72,168],2)
    fun.Rectangulo(MyWindow,Black,[0,168],[72,240],2)
    fun.Rectangulo(MyWindow,Black,[0,240],[72,312],2)
    fun.Rectangulo(MyWindow,Black,[0,312],[72,384],2)
    fun.Rectangulo(MyWindow,Black,[0,384],[72,456],2)
    fun.Rectangulo(MyWindow,Black,[0,456],[72,528],2)
    #figures from the boxes
    fun.Linea(MyWindow,Black,[15,109],[57,151],2)
    fun.Rectangulo(MyWindow,Black,[11,194],[61,214],2)
    fun.Rectangulo(MyWindow,Black,[11,266],[61,296],0)
    fun.Circulo(MyWindow,Black,36,348,20,2)
    pygame.draw.circle(MyWindow,Black,[36,420],20,0)
    pygame.draw.polygon(MyWindow, Black,[(11,512), (61,512), (36,472)],2)
    fun.draw_regular_polygon(MyWindow, Black, 5,20, (36,564))
    MyWindow.blit(paleta,(0,25))
    
    
if __name__ == '__main__':
    MyWindow = pygame.display.set_mode((800,600))
    MyWindow.fill(White)
    Running = True
    Cont = 0 
    Figure = "Pencil"
    color = LightGrey
    while(Running):
        Barras(MyWindow)
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                Running = False
                exit()
            if Event.type == pygame.MOUSEBUTTONDOWN:
                x,y = Event.pos
                if ((x >= 0 and y >= 0 and x <= 800 and y <= 80) or (x >= 0 and y >= 25 and x <= 72 and y <= 600)):
                    color = SelectColor(x,y,Figure,color)
                    Figure = SelectFigure(x,y,Figure,color)
                    print("x: ",x,"y: ",y," ",Figure," ",color)
                if x > 72 and y > 24 and x < 800 and y < 600:
                    #Line
                    if Figure == "Line":
                        if Cont < 2:
                            if Cont == 0:
                                x1,y1 = Event.pos
                                print("Line punto ",Cont+1,"x:",x1," y:",y1)
                                Cont += 1
                            elif Cont == 1:
                                x2,y2 = Event.pos
                                print("Line Punto: ",Cont+1," x:",x2," y:",y2)
                                Cont += 1
                        
                        if Cont == 2:
                            
                            pygame.draw.line(MyWindow,color,(x1,y1),(x2,y2),2)
                            Cont = 0
                            print("Line")
                            x=0
                            y=0
                    #Rectangle fill
                    elif Figure == "Rect":
                        if Cont < 2:
                            if Cont == 0:
                                x1,y1 = Event.pos
                                print("Line punto ",Cont+1,"x:",x1," y:",y1)
                                Cont += 1
                            elif Cont == 1:
                                x2,y2 = Event.pos
                                print("Line Punto: ",Cont+1," x:",x2," y:",y2)
                                Cont += 1
                        if Cont == 2:
                            fun.Rectangulo(MyWindow,color,[x1,y1],[x2,y2],2)
                            Cont = 0
                            print("Rectangulo")
                    #Rectangle fill
                    elif Figure == "RectFill":
                        if Cont < 2:
                            if Cont == 0:
                                x1,y1 = Event.pos
                                print("Line punto ",Cont+1,"x:",x1," y:",y1)
                                Cont += 1
                            elif Cont == 1:
                                x2,y2 = Event.pos
                                print("Line Punto: ",Cont+1," x:",x2," y:",y2)
                                Cont += 1
                        if Cont == 2:
                            fun.Rectangulo(MyWindow,color,[x1,y1],[x2,y2],0)
                            Cont = 0
                            print("Rectangulo")
                    #Circle
                    elif Figure == "Cir":
                        if Cont < 2:
                            if Cont == 0:
                                x1,y1 = Event.pos
                                print("Line punto ",Cont+1,"x:",x1," y:",y1)
                                Cont += 1
                            elif Cont == 1:
                                x2,y2 = Event.pos
                                print("Line Punto: ",Cont+1," x:",x2," y:",y2)
                                Cont += 1
                        if Cont == 2:
                            r = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
                            fun.Circulo(MyWindow,color,x1,y1,r,2)
                            Cont = 0
                            print("Circulo")
                    #Cicle fill    
                    elif Figure == "CirFill":
                        if Cont < 2:
                            if Cont == 0:
                                x1,y1 = Event.pos
                                print("Line punto ",Cont+1,"x:",x1," y:",y1)
                                Cont += 1
                            elif Cont == 1:
                                x2,y2 = Event.pos
                                print("Line Punto: ",Cont+1," x:",x2," y:",y2)
                                Cont += 1
                        if Cont == 2:
                            r = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
                            pygame.draw.circle(MyWindow,color,[x1,y1],r,0)
                            Cont = 0
                            print("Circulo lleno")
                    #Triangle
                    elif Figure == "Triangle":
                        x3=0
                        y3=0
                        if Cont < 3:
                            if Cont == 0:
                                x1,y1 = Event.pos
                                print("Line punto ",Cont+1,"x:",x1," y:",y1)
                                Cont += 1
                            elif Cont == 1:
                                x2,y2 = Event.pos
                                print("Line Punto: ",Cont+1," x:",x2," y:",y2)
                                pygame.draw.line(MyWindow,color,(x1,y1),(x2,y2),2)
                                Cont += 1
                            elif Cont == 2:
                                x3,y3 = Event.pos
                                print("Line Punto: ",Cont+1," x:",x3," y:",y3)
                                pygame.draw.line(MyWindow,color,(x2,y2),(x3,y3),2)
                                pygame.draw.line(MyWindow,color,(x3,y3),(x1,y1),2)
                                Cont = 0
                                print("Triangle")
                                
                    elif Figure == "Penta":
                        radio = 0
                        if Cont < 2:
                            if Cont == 0:
                                x1,y1 = Event.pos
                                print("Line punto ",Cont+1,"x:",x1," y:",y1)
                                Cont += 1
                            elif Cont == 1:
                                x2,y2 = Event.pos
                                posIni = x1+y1
                                PosFinal = x2+y2
                                radio = ((posIni+PosFinal)/6) 
                                Cont += 1
                        if Cont == 2:
                            r = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
                            print("Line punto ",Cont+1,"x:",x1," y:",y1)
                            fun.draw_regular_polygon(MyWindow, color, 5,r, (x1, y1))
                            print("Pentagono")
                            Cont = 0        
                            
                    elif Figure == "Lapiz":
                        veces = 0
                        onClick = True
                        while onClick and veces  < 1:
                            mouse_pos = pygame.mouse.get_pos()
                            for e in pygame.event.get():
                                if e.type == pygame.QUIT:
                                    break
                                if e.type == pygame.MOUSEBUTTONUP:
                                    line_start = None if line_start else mouse_pos
                                    onClick = False
                                    veces +=1
                            else:
                                if line_start:
                                    pygame.draw.line(MyWindow, color, line_start, mouse_pos, 3)
                                    line_start = mouse_pos
                                pygame.display.flip()
                                continue
                            break       
                            
                            
                            
            pygame.display.update()
                            
                            