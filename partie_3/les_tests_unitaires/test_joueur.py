import unittest
from partie_3.championnat.personnel.joueur import Joueur


class MyTestCase(unittest.TestCase):
    def test_something(self):

        # Arrange
        joueur = Joueur("messi", "lionnel", 34, "attaquant", 10) # Instanciation d'un objet joueur

        # Act
        joueur.donnerJaune()  # Premier carton
        joueur.marquerBut() # Un but marqué
        joueur.donnerJaune() # Deuxieme jaune
        joueur.donnerRouge() # Carton rouge
        joueur.donnerPoste("milieu offensif") # Enregistrement du poste du joueur

        # Assert
        self.assertEqual(joueur.nombreDeJaunes, 2) # Test de l'automatisation du compteur de carton jaune pris par le joueur
        self.assertEqual(joueur.nombreDeButs, 1) # Test de l'automatisation du compteur de but marqué apr le joueur
        self.assertEqual(joueur.nombreDeRouges, 1) # Test de l'automatisation du compteur de carton rouge pris par le joueur
        self.assertEqual("milieu offensif", joueur.poste) # Test de vérification du poste du joueur

        # < Communication entre les classes Personne et Arbitre >
        # Test de la methode affichage de Personne redefinie dans Arbitre avec notre simulateur infoStaffRedéfinitionSimple()
        self.assertEqual(joueur.infoStaffRedéfinitionSimple(), "nom: messi, prenom: lionnel, age: 34 ans")


if __name__ == '__main__':
    unittest.main()
