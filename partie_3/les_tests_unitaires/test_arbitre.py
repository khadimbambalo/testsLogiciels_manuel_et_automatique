import unittest
from partie_3.championnat.personnel.arbitre import Arbitre


# Bibliotheque importées pour la création de nos simulateurs
from partie_3.championnat.organisation.equipe import Equipe
from partie_3.championnat.organisation.match import Match

# Correction: Ajouter à la version 2 pour la partie 3 permettant de mettre à jour le championnat juste aprés le coup final de l'arbitre
from partie_3.championnat.organisation.championnat import Championnat

# Simulateurs match et joueur pour tester certaines methodes de la classe "Equipe"
barca = Equipe("barca")
real = Equipe("real")
match = Match(barca, real)

# Correction: Version 2 pour tester la partie 3
championnat = Championnat("liga", "espagne")
championnat.ajoutMatch(match)



class MyTestCase(unittest.TestCase):
    def test_something(self):

        # Arrange
        arbitre  = Arbitre("ba", "malick", 38) # Instanciation d'un objet arbitre

        # Act
        nouveauPoste = "central"
        arbitre.affectation(nouveauPoste) # Assignation de poste à l'arbitre
        match.ajouArbitre(arbitre)
        arbitre.matchTerminer(barca, real, 3, 1) # Le coup de sifflet final de l'arbitre

        # Assert
        self.assertEqual("central", arbitre.poste) # test de l'assignation de poste à l'arbitre
        # < Communication entre les classes Personne et Arbitre >
        # Test de la methode affichage de Personne redefinie dans Arbitre avec notre simulateur infoStaffRedéfinitionSimple()
        self.assertEqual(arbitre.infoStaffRedéfinitionSimple(), "nom: ba, prenom: malick, age: 38 ans")
        # Vérifier si les données du classement et des équipes sont mises à jour aprés le sifflet final de l'arbitre
        self.assertEqual(barca.nombreDePoints, 3) # Chaque equipe gagne 3 points aprés une victoire
        self.assertEqual(barca.nombreDeVictoires, 1) # Le nombre de victoire s'incrémente et permet de creer le nombre points
        self.assertEqual(real.nombreDeDefaites, 1) # On enregistre aussi le nombre de défaite de chaque pour les statistiques




if __name__ == '__main__':
    unittest.main()
