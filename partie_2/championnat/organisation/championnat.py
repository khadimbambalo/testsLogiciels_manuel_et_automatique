from partie_2.championnat.organisation.equipe import Equipe
from partie_2.championnat.organisation.match import Match

class Championnat:
    programes = []
    equipes = []
    def __init__(self, nom, pays):
        self.nom = nom
        self.pays = pays
        self.programes = Championnat.programes # une liste de rencontres
        self.equipes = Championnat.equipes # Equipes du championnat

    def ajoutEquipe(self, equipe:Equipe):
        self.equipes.append(equipe)

    def ajoutMatch(self, macth:Match):
        self.programes.append(macth)

    def classement(self):
        sorted(self.equipes, key=lambda equipe:equipe.nombreDePoints)
        i = 1
        for equipe in self.equipes:
            equipe.rang = i
            print(f"rang: {i}, Nom: {equipe.nom}, nombre de points: {equipe.nombreDePoints}")
            i += 1

