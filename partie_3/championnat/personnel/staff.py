from partie_3.championnat.personnel.personne import Personne


class Staff(Personne):

    def __init__(self, nom, prenom, age):
        super().__init__(nom, prenom, age)
        self.role = ""
        self.equipe = ""

    def doonerRole(self, role):
        self.role = role

    def infoStaff(self):
        return super().affichage() + ", role: " + self.role + ", equipe: " + self.equipe.nom

    # Cette methode est définie juste pour tester la communication entre Personne et Staff pour la methode affichage, c'est un simulateur
    def infoStaffRedéfinitionSimple(self):
        return super().affichage()
