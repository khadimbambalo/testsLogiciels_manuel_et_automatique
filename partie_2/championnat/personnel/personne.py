class Personne:

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom =prenom
        self.age  = age

    def affichage(self):
        return "nom: " + self.nom + ", prenom: " + self.prenom + ", age: " + str(self.age) + " ans"
