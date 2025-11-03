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
        self.delai_creation_max = 20
        self.delai_creation = 0
        self.points = None
        self.ballounes = []

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