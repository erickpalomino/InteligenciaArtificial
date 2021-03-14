from turtle import *
import random
import math
from Cuadrado import *
from Pacman import *
escenario=[]
global pacman 

def generarEscenario():
    for i in range(7):
        for j in range(7):
            escenario.append(Cuadrado(5,True,-300+100*j,300-100*i,[0]))
    escenario[0].setVecinos([1,7])
    escenario[1].setVecinos([0,2])
    escenario[2].setVecinos([1])
    escenario[3].volverTrampa()
    escenario[4].setVecinos([11,5])
    escenario[5].setVecinos([4])
    escenario[7].setVecinos([0,14])
    for i in range(3):
        escenario[8+i].volverTrampa()
    escenario[11].setVecinos([4,18])
    escenario[12].volverTrampa()
    escenario[14].setVecinos([15])
    escenario[15].setVecinos([14,16,22])
    escenario[16].setVecinos([15,23])
    escenario[17].volverTrampa()
    escenario[18].setVecinos([11,25])
    escenario[19].volverTrampa()
    escenario[21].volverTrampa()
    escenario[22].setVecinos([15,23,29])
    escenario[23].setVecinos([16,22,24])
    escenario[24].setVecinos([25,23])
    escenario[25].setVecinos([24,18,26,32])
    escenario[26].setVecinos([25])
    escenario[28].volverTrampa()
    escenario[29].setVecinos([22,36])
    for i in range (2):
        escenario[30+i].volverTrampa()
    escenario[32].setVecinos([25,39])
    escenario[33].volverTrampa()
    escenario[35].setVecinos([36])
    escenario[36].setVecinos([29,35,37])
    escenario[37].setVecinos([36,38])
    escenario[38].setVecinos([37,39,45])
    escenario[39].setVecinos([38,40])
    escenario[40].setVecinos([39])
    escenario[45].setVecinos([38])
    for i in range(7):
        escenario[(7*(i+1))-1].volverTrampa()
    
    for i in range(3):
        escenario[42+i].volverTrampa()
        escenario[46+i].volverTrampa()
    escenario[45].meta=True

    for i in range(49):
        escenario[i].vecinos.sort(reverse=True)
        escenario[i].id=i
def dibujarEscenario():
    delay(0)
    for cuadrado in escenario:
        print(cuadrado.vecinos)
        cuadrado.dibujar()

def generarPacman():
    global pacman
    pacman=Pacman(escenario[0],escenario[45])
    pacman.analizarDFS(escenario,escenario[0])


def dibujarPacman():
    delay(0)
    pacman.dibujar()

def Mover():
    delay(50)
    pacman.recorrerCaminoDFS(escenario)

def main ():
    setup(1200,700)
    generarEscenario()
    dibujarEscenario()
    generarPacman()
    dibujarPacman()
    pacman.verVisitados()
    Mover()
    input()


main()
input()


