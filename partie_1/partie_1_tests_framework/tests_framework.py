import unittest
from partie_1.partie_1_tests_generes.calcul import Calculatrice


class Test_Calculatrice(unittest.TestCase):

    # Définition de la méthode test de l'addition
    def test_addition(self):
        # Arrange
        machine = Calculatrice(5,1)
        # Act
        resultat = machine.addition()
        # Assert
        self.assertEqual(resultat, 6)

    # Définition de la méthode test de soustraction
    def test_soustraction(self):
        # Arrange
        machine = Calculatrice(5, 1)
        # Act
        resultat = machine.soustraction()
        # Assert
        self.assertEqual(resultat, 4)

    # Définition de la méthode test de la division
    def test_division(self):
        # Arrange
        machine = Calculatrice(5, 1)
        # Act
        resultat = machine.division()
        # Assert
        self.assertEqual(resultat, 5)

    # Définition de la méthode test de multiplication
    def test_multiplication(self):
        # Arrange
        machine = Calculatrice(5, 1)
        # Act
        resultat = machine.multiplication()
        # Assert
        self.assertEqual(resultat, 5)


if __name__ == '__main__':
    unittest.main()

