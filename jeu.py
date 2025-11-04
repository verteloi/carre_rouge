import tkinter as tk
import random as rd

class Balloune():
    def __init__(self, parent, pos_x, pos_y):
        self.parent = parent
        self.pos_x = pos_x
        self.pos_y = pos_y

class Modele():
    def __init__(self, parent, largeur, hauteur):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.carree = Carree(self, 40, 255, 255)
        self.rectangle1 = Rectangle(self, 60, 60, 100, 100)
        self.rectangle2 = Rectangle(self, 60, 50, 300, 85)
        self.rectangle3 = Rectangle(self, 30, 60, 85, 350)
        self.rectangle4 = Rectangle(self, 100, 20, 355, 340)

class Carree():
    def __init__(self, parent, dimension, posX, posY):
        self.parent = parent
        self.dimension = dimension
        self.posX = posX
        self.posY = posY
        self.couleur = "rouge"

class Rectangle():
    def __init__(self, parent, largeur, hauteur, posX, posY, vitesse):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.posX = posX
        self.posY = posY
        self.couleur = "bleue"
        self.vitesse = vitesse

class Border():
    def __init__(self, parent, largeur, hauteur, posX, posY):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.posX = posX
        self.posY = posY
        self.couleur = "noire"

class Vue():
    def __init__(self, parent, largeur, hauteur):         # c'est une convention de dire self mais c'est une variable comme une autre
        self.parent = parent
        self.root = tk.Tk()
        self.largeur = largeur
        self.hauteur = hauteur
        self.creer_interface()

class Controleur():                     # Normalement entre le () se trouve ce que la classe hétrite (une autre class par ex.)
    def __init__(self):    
        self.vue = Vue(self, largeur=800, hauteur=600)            # je passe self pour que la vue puisse me parler au besoin
        self.modele = Modele(self, largeur=800, hauteur=600)
        self.vue.root.mainloop()

if __name__ == "__main__":
    c = Controleur()