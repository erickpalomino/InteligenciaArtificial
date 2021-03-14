from turtle import *
import random
import math
from Cuadrado import *

class Pacman (Turtle):
    def __init__(self,inicio,meta):
        Turtle.__init__(self)
        self.inicio=inicio
        self.meta=meta
        self.visitados=list()
        self.queue=[]
        self.caminoEncontrado=False

    def dibujar(self):
        self.fillcolor("yellow")
        self.penup()
        self.sety(self.inicio.coordY)
        self.setx(self.inicio.coordX)
        self.shape("circle")
        self.shapesize(3,3)

    def analizarDFS(self,grafo,nodo):
        delay(100)
        if (nodo not in self.visitados) and (not self.caminoEncontrado) :
            nodo.fillcolor("green")
            if nodo.meta:
                self.caminoEncontrado=True
                nodo.fillcolor("red")
            self.visitados.append(nodo)
            for vecinos in nodo.getVecinos():
                grafo[vecinos].anterior=nodo.id
                self.analizarDFS(grafo,grafo[vecinos])

    def verVisitados(self):
        for nodo in self.visitados:
            print(nodo.id)

    def recorrerCaminoDFS(self,escenario):
        for i in self.visitados:
            self.goto(escenario[i.id].coordX,escenario[i.id].coordY)