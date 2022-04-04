from partie_3.championnat.personnel.joueur import Joueur
from partie_3.championnat.personnel.staff import Staff

class Equipe:
    joueurs = []
    staff = []
    nombreDeVictoires = 0
    nombreDeDefaites = 0
    nombreDePoints =0
    rang = 0
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = Equipe.joueurs
        self.nombreDeVictoires = Equipe.nombreDeVictoires
        self.nombreDeDefaites= Equipe.nombreDeDefaites
        self.nombreDePoints = Equipe.nombreDePoints
        self.fond = 0
        self.rang = Equipe.rang

    def ajoutJoueur(self, joueur:Joueur):
        self.joueurs.append(joueur)
        joueur.equipe = self

    def recruter(self, staff:Staff):
        self.staff.append(staff)
        staff.equipe = self

    def payerJoueur(self, joueur:Joueur, salaire):
        joueur.fortune += salaire
        self.fond -= salaire

    def enregistrerPrime(self, prime):
        self.fond += prime


    def infosEquipe(self):
        print(f"nom: {self.nom}, nombre de points: {self.nombreDePoints},"
              f" nombre de victoires: {self.nombreDeVictoires}, nombre de defaites: {self.nombreDeDefaites} rang: {self.rang}")
        for joueur in self.joueurs:
            print(f"joueurs: {joueur.nom}, {joueur.prenom}, {joueur.numero}, {joueur.poste}")



