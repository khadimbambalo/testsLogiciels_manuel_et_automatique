from partie_2.championnat.organisation.equipe import Equipe
#from partie_2.championnat.organisation.match import Match
from partie_2.championnat.personnel.personne import Personne

class Arbitre(Personne):

    # Partie_3: Ajout ou supression d'un attribut "ajout" (donné et non donné) au constructeur mére
    def __init__(self, nom, prenom, age):
        super().__init__(nom, prenom, age)
        self.match = "Non definiNon defini"
        self.poste = "Non defini"
        self.credit = 0

    def affectation(self, affectation):
        self.poste = affectation

    def matchTerminer(self, equipe_1:Equipe, equipe_2:Equipe, score_1:int, score_2:int):
        self.match.miseAJourResultat(equipe_1, equipe_2, score_1, score_2)

    def infoArbitre(self):
        return super().affichage() + ", affectation: " + self.poste + ", credit: " + str(self.credit) + ", match: " + self.match.infoMatch()

    def infoStaffRedéfinitionSimple(self):
        return super().affichage()