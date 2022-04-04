from partie_3.championnat.organisation.equipe import Equipe
#from partie_3.championnat.organisation.championnat import Championnat
from partie_3.championnat.personnel.arbitre import Arbitre
class Match:
    vainqueur: Equipe
    vaincu: Equipe
    arbitre:Arbitre = Arbitre("Non défini", "Non défini", "Non défini")
    lieu = "Non défini"
    date = "Non défini"

    def __init__(self, equipe_A:Equipe, equipe_B:Equipe):
        self.equipe_A = equipe_A
        self.equipe_B = equipe_B
        self.lieu = Match.lieu
        self.date = Match.date
        self.championnat = ""


    def ajoutLieu(self, lieu):
        self.lieu = lieu

    def ajoutDate(self, date):
        self.date = date

    def ajouArbitre(self, arbitre:Arbitre):
        self.arbitre = arbitre
        arbitre.match = self

    def miseAJourResultat(self, equipe_1:Equipe, equipe_2:Equipe, score_1:int, score_2:int):
        if score_1 > score_2:
            equipe_1.nombreDeVictoires += 1
            equipe_1.nombreDePoints += 3
            equipe_2.nombreDeDefaites += 1
            self.vainqueur = equipe_1
            self.vaincu = equipe_2
        elif score_1 < score_2:
            equipe_2.nombreDeVictoires += 1
            equipe_2.nombreDePoints += 3
            equipe_1.nombreDeDefaites += 1
            self.vainqueur = equipe_2
            self.vaincu = equipe_1
        elif score_1 == score_2:
            equipe_1.nombreDePoints += 1
            equipe_2.nombreDePoints += 1
        self.arbitre.credit += 1
        self.championnat.classement()


    def infoMatch(self):
        return self.equipe_A.nom +  " VS " + self.equipe_B.nom + " au " + self.lieu

