# Création de la classe test
class Calculatrice:
    # Création du constructeur
    def __init__(self, variable_1: float, variable_2: float):
        self.variable_1 = variable_1
        self.variable_2 = variable_2

    # Création de la méthode addition
    def addition(self):
        return self.variable_1 + self.variable_2

    # Création de la méthode soustraction
    def soustraction(self):
        return self.variable_1 - self.variable_2

    # Création de la méthode division
    def division(self):
        try:
            return self.variable_1 / self.variable_2
        except ZeroDivisionError:
            print("Valeur invalide")

    # Création de la méthode multiplication
    def multiplication(self):
        return self.variable_1 * self.variable_2




