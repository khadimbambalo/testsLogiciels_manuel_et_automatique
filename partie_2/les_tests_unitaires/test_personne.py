import unittest
from partie_2.championnat.personnel.personne import Personne

"""
La classe personne, elle est heritée par les clases Joueur, Arbitre et Staff
La méthode affichage de Personne a été redéfinie dans ces clases là
Cette classe Personne est indépendante de toutes les classes
"""

class MyTestCase(unittest.TestCase):

    def test_personne(self):
        # Arrange
        personne  = Personne("lo", "khadim", 23) #test du constructeur
        # Act
        affichage = personne.affichage()
        # Assert
        self.assertEqual("nom: lo, prenom: khadim, age: 23 ans", affichage) # Test de la methode affichage


if __name__ == '__main__':
    unittest.main()
