from turtle import *
import random
import math
class Cuadrado (Turtle):
    def __init__(self,lado,accesible,coordX,coordY,vecinos):
        Turtle.__init__(self)
        self.id=0
        self.lado=lado
        self.accesible=accesible
        self.coordX=coordX
        self.coordY=coordY
        self.vecinos=vecinos
        self.meta=False
        self.anterior=0
    
    def setVecinos(self, vecinos):
        self.color("white")
        self.vecinos=vecinos

    def getVecinos(self):
        return self.vecinos
    
    def volverTrampa(self):
        self.accesible=False
        self.color("gray")

    def dibujar(self):
        self.pencolor("black")
        self.pensize(2)
        self.penup()
        self.sety(self.coordY)
        self.setx(self.coordX)
        self.shape("square")
        self.shapesize(self.lado,self.lado)
        self.write(self.id,align="left",font=("arial",10,"normal"))

    def cambiarColor(self,color):
        self.color(color)




