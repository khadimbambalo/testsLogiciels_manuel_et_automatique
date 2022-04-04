from partie_3.championnat.personnel.personne import Personne

class Joueur(Personne):

    def __init__(self, nom, prenom, age, poste, numero:int):
        super().__init__( nom, prenom, age)
        self.poste = poste
        self.numero = numero
        self.equipe = "Joueur libre"
        self.nombreDeJaunes = 0
        self.nombreDeRouges = 0
        self.nombreDeButs = 0
        self.fortune = 0

    def donnerPoste(self, poste):
        self.poste = poste

    def donnerJaune(self):
        self.nombreDeJaunes += 1

    def donnerRouge(self):
        self.nombreDeRouges += 1

    def marquerBut(self):
        self.nombreDeButs += 1

    def infoJoueur(self):
        return super().affichage() + ", equipe: " + self.equipe.nom + ", carton jaunes: " + str(self.nombreDeJaunes) + ", carton rouges: " + str(self.nombreDeRouges) + ", nombre de buts: " + str(self.nombreDeButs)

    # Cette methode est définie juste pour tester la communication entre Personne et Staff pour la methode affichage, c'est un simulateur
    def infoStaffRedéfinitionSimple(self):
        return super().affichage()
