import tkinter as tk

class Modele():
    def __init__(self, parent, largeur, hauteur):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.carre = Carre(self, 40, 185, 185)
        self.rectangles = [
            Rectangle(self, 50, 50, 75, 75, 5),
            Rectangle(self, 50, 40, 270, 65, 5),
            Rectangle(self, 30, 60, 70, 280, 5),
            Rectangle(self, 100, 20, 230, 300, 5)
        ]

class Carre():
    def __init__(self, parent, dimension, posX, posY):
        self.parent = parent
        self.dimension = dimension
        self.posX = posX
        self.posY = posY
        self.couleur = "red"

class Rectangle():
    def __init__(self, parent, largeur, hauteur, posX, posY, vitesse):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.posX = posX
        self.posY = posY
        self.couleur = "blue"
        self.vitesse = vitesse
        self.direction = 1

    def bouger_rectangles(self, largeur, hauteur):
        self.posX += self.vitesse * self.direction
        # if self.posX <= 0

class Vue:
    def __init__(self, parent, largeur, hauteur):
        self.parent = parent
        self.largeur = largeur
        self.hauteur = hauteur
        self.root = tk.Tk()
        self.creer_interface()
        self.canvas.bind("<Button-1>", self.parent.detecter_clique)

    def creer_interface(self):
        self.canvas = tk.Canvas(self.root, width=self.largeur, height=self.hauteur, bg="gray")
        self.canvas.pack()
        self.canvas.create_rectangle(50, 50, self.largeur - 50, self.hauteur - 50, fill="white")
        posXCarre,posYCarre,dimensionCarre,couleurCarre = self.parent.info_carre()

        posXRect1, posYRect1, hauteurRect1, largeurRect1, couleurRect1 = self.parent.info_rectangle1()
        posXRect2, posYRect2, hauteurRect2, largeurRect2, couleurRect2 = self.parent.info_rectangle2()
        posXRect3, posYRect3, hauteurRect3, largeurRect3, couleurRect3 = self.parent.info_rectangle3()
        posXRect4, posYRect4, hauteurRect4, largeurRect4, couleurRect4 = self.parent.info_rectangle4()
        
        self.canvas.create_rectangle(posXCarre, posYCarre, posXCarre + dimensionCarre, posYCarre + dimensionCarre, fill=couleurCarre)

        self.canvas.create_rectangle(posXRect1, posYRect1, posXRect1 + largeurRect1, posYRect1 + hauteurRect1, fill=couleurRect1)
        self.canvas.create_rectangle(posXRect2, posYRect2, posXRect2 + largeurRect2, posYRect2 + hauteurRect2, fill=couleurRect2)
        self.canvas.create_rectangle(posXRect3, posYRect3, posXRect3 + largeurRect3, posYRect3 + hauteurRect3, fill=couleurRect3)
        self.canvas.create_rectangle(posXRect4, posYRect4, posXRect4 + largeurRect4, posYRect4 + hauteurRect4, fill=couleurRect4)   

    def afficher_scores(self):
        pass

class Controleur():                     # Normalement entre le () se trouve ce que la classe hétrite (une autre class par ex.)
    def __init__(self):    
        self.modele = Modele(self, largeur=400, hauteur=400)
        self.vue = Vue(self, largeur = self.modele.largeur, hauteur=self.modele.hauteur)            # je passe self pour que la vue puisse me parler au besoin
        self.vue.root.mainloop()

    def info_carre(self):
        return self.modele.carre.posX, self.modele.carre.posY, self.modele.carre.dimension, self.modele.carre.couleur

    def info_rectangle1(self):
        return self.modele.rectangles[0].posX, self.modele.rectangles[0].posY, self.modele.rectangles[0].hauteur, self.modele.rectangles[0].largeur, self.modele.rectangles[0].couleur

    def info_rectangle2(self):
        return self.modele.rectangles[1].posX, self.modele.rectangles[1].posY, self.modele.rectangles[1].hauteur, self.modele.rectangles[1].largeur, self.modele.rectangles[1].couleur

    def info_rectangle3(self):
        return self.modele.rectangles[2].posX, self.modele.rectangles[2].posY, self.modele.rectangles[2].hauteur, self.modele.rectangles[2].largeur, self.modele.rectangles[2].couleur

    def info_rectangle4(self):
        return self.modele.rectangles[3].posX, self.modele.rectangles[3].posY, self.modele.rectangles[3].hauteur, self.modele.rectangles[3].largeur, self.modele.rectangles[3].couleur
    
    def detecter_clique(self, event):
        carre = self.modele.carre
        if (carre.posX <= event.x <= carre.posX + carre.dimension and carre.posY <= event.y <= carre.posY + carre.dimension):
            self.jouer()

    def jouer():
        while True:
            pass

if __name__ == "__main__":
    c = Controleur()
