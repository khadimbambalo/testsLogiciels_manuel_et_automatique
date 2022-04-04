import unittest
from partie_3.championnat.organisation.equipe import Equipe

# Bibliotheque importées pour la création de nos simulateurs
from partie_3.championnat.personnel.joueur import Joueur
from partie_3.championnat.personnel.staff import Staff

# Simulateurs staff et joueur pour tester certaines methodes de la classe "Equipe"
entraineur = Staff("lo", "khadim", 57)
adjoint = Staff("flageol", "william", 67)
messi = Joueur("messi", "lionnel", 34, "attaquant", 10)


class MyTestCase(unittest.TestCase):

    def test_something(self):

        # Arrange
        equipe = Equipe("Paris") # Instanciation d'un objet equipe au nom de paris

        # Act
        equipe.ajoutJoueur(messi) # Recrutement d'un joueur par l'équipe
        equipe.recruter(entraineur) # Recrutement d'un entraineur pour l'équipe
        equipe.recruter(adjoint) # Recrutement d'un adjoint pour l'équipe
        equipe.enregistrerPrime(230000) # Accord d'un prime à l'équipe
        equipe.payerJoueur(messi, 5000) # Payement des joueurs par l'équipe

        # Assert
        self.assertEqual(equipe.joueurs[0].nom, "messi") # Vérification du nom d'un joueur précis de l'équipe
        self.assertEqual(equipe.joueurs[0].age, 34) # Vérification de l'âge d'un joueur précis de l'équipe
        self.assertEqual(equipe.staff[0].nom, "lo") # Vérification du nom d'un staff précis de l'équipe
        self.assertEqual(equipe.joueurs[0].fortune, 5000) # Vérification du compte de payement d'un joueur de l'équipe
        self.assertEqual(equipe.fond, 230000-5000) # Vérification du fond de l'équipe aprés payement des joueurs


if __name__ == '__main__':
    unittest.main()
