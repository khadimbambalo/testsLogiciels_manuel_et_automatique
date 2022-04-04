import unittest
from partie_3.championnat.personnel.staff import Staff

"""
La classe Staff hérite tout simplement de la classe Personne et va redéfinir sa méthode affichge pour afficher lui aussi
On va tester l'instanciation d'un objet Staff et l'affichage de ses informations pour voir si l'interaction avec 
la classe Personne marchent correctement 
"""

class MyTestCase(unittest.TestCase):
    def test_something(self):

        # Arrange
        staff  = Staff("pep", "gardiola", 56) # Instanciation d'un objet staff

        # Act
        poste = "entraineur" # On definit un rôle à assigner au nouveau staff
        staff.doonerRole(poste) # On assigne un rôle au nouveau staff recrutè

        # Assert
        self.assertEqual(staff.role, "entraineur") # Test de l'assignation

        # < Communication entre les classes Personne et Arbitre >
        # Test de la methode affichage de Personne redefinie dans Staff avec notre simulateur infoStaffRedéfinitionSimple()
        self.assertEqual(staff.infoStaffRedéfinitionSimple(), "nom: pep, prenom: gardiola, age: 56 ans")




if __name__ == '__main__':
    unittest.main()
