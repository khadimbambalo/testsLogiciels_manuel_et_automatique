class Personne:

    # Parite_3: Ajout d'un parametre "ajout" dans le constructeur de la classe héritée
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom =prenom
        self.age  = age
        #self.ajout = ajout

    def affichage(self):
        return "nom: " + self.nom + ", prenom: " + self.prenom + ", age: " + str(self.age) + " ans"
