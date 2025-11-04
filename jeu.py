import tkinter as tk

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

class Vue:
    def __init__(self, parent, largeur, hauteur):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        

        self.root = tk.Tk()
        

        self.creer_interface()

    def creer_interface(self):
        self.canvas = tk.Canvas(self.root, width=self.largeur, height=self.hauteur, bg="gray")
        self.canvas.pack()
        self.canvas.create_rectangle(50, 50, self.largeur - 50, self.hauteur - 50, fill="white")


    def afficher_scores(self):
        pass

class Controleur():                     # Normalement entre le () se trouve ce que la classe hétrite (une autre class par ex.)
    def __init__(self):    
        self.modele = Modele(self, largeur=400, hauteur=400)
        self.vue = Vue(self, largeur = self.modele.largeur, hauteur=self.modele.hauteur)            # je passe self pour que la vue puisse me parler au besoin
        self.vue.root.mainloop()


if __name__ == "__main__":
    c = Controleur()
