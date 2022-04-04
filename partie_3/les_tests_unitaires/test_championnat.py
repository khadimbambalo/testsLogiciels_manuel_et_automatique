import unittest
from partie_3.championnat.organisation.championnat import Championnat

# Bibliotheque importées pour la création de nos simulateurs
from partie_3.championnat.organisation.equipe import Equipe
from partie_3.championnat.organisation.match import Match
from partie_3.championnat.personnel.arbitre import Arbitre

# Simulateurs equipe et match pour tester certaines methodes de la classe "Championnat"
barca = Equipe("barca")
real = Equipe("real")
match = Match(barca, real)
arbitre = Arbitre("colina", "michel", 45)
match.ajouArbitre(arbitre)


class MyTestCase(unittest.TestCase):

    def test_something(self):

        # Arrange
        liga = Championnat("Liga", "Espagne") # Creation d'un championnat

        # Act
        liga.ajoutEquipe(barca) # Accueil de l'equipe barca dans le championnat
        liga.ajoutEquipe(real) # Accueil de l'equipe real dans le championnat
        liga.ajoutMatch(match) # Organisation d'un match dans le championnat
        liga.programes[0].arbitre.matchTerminer(barca, real, 2, 0) # Coup de sifflet final de l'arbitre
        liga.classement()

        # Assert
        self.assertEqual(liga.equipes[0].nom, "barca")
        self.assertEqual(liga.equipes[1].nom, "real")
        self.assertEqual(liga.nom, "Liga")

        # < Communication entre les classes Match, Equipe, Arbitre et Championnat >
        self.assertEqual(liga.programes[0].arbitre.credit, 2)
        self.assertEqual(liga.programes[0].vainqueur.nombreDePoints, 3)
        self.assertEqual(liga.programes[0].vainqueur.rang, 1)


if __name__ == '__main__':
    unittest.main()
