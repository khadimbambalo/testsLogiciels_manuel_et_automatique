from partie_3.championnat.organisation.equipe import Equipe
from partie_3.championnat.organisation.match import Match

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

    def ajoutMatch(self, match:Match):
        self.programes.append(match)
        match.championnat = self


    """
    Ajout d'une fonctionnalité avec une classe imbriquée 
    Creation de la classe interne "SuperCoupe" qui est une compétition eliminatoire des 4 meilleures équipes
    """
    class SuperCoupe:
        match_1:Match = ""
        match_2:Match = ""
        participants = []
        def __init__(self, equipes:[]):
            equipes.sort(key=lambda equipe: equipe.nombreDePoints, reverse=True)
            for i in range(4):
                self.participants.append(equipes[i])
        def organiserMatch(self):
            match_1 = Match(self.participants[0], self.participants[1])
            self.match_1 = match_1
            match_2 = Match(self.participants[2], self.participants[3])
            self.match_2 = match_2
            print(match_1.infoMatch() + " et " + match_2.infoMatch())


    def classement(self):
        self.equipes.sort(key=lambda equipe:equipe.nombreDePoints, reverse=True)
        i = 1
        for equipe in self.equipes:
            equipe.rang = i
            print(f"rang: {i}, Nom: {equipe.nom}, nombre de points: {equipe.nombreDePoints}")
            i += 1

    # Creer de notre fameuse super coupe des meilleures 4 équipes
    def superCoupe(self):
        self.super_coupe = self.SuperCoupe(self.equipes)
        self.super_coupe.organiserMatch()

