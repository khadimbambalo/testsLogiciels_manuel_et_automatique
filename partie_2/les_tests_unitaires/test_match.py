import unittest
from partie_2.championnat.organisation.match import Match


# Bibliotheque importées pour la création de nos simulateurs
from partie_2.championnat.organisation.equipe import Equipe
from partie_2.championnat.personnel.arbitre import Arbitre

# Simulateurs equipe et arbitre pour tester certaines methodes de la classe "Match"
arbitre = Arbitre("peres", "l'arbitre", 45)
barca = Equipe("barca")
real = Equipe("real")


class MyTestCase(unittest.TestCase):
    def test_something(self):

        # Arrange
        match = Match(barca, real)

        # Act
        match.ajoutLieu("quebec")
        match.ajouArbitre(arbitre)

        # < Communication entre les classes Match et Arbitre >
        match.arbitre.matchTerminer(barca, real, 2, 1) # Cette méthode appelle directement la meéthode miseAJourResultat() de la classe Match

        # Assert
        self.assertEqual(match.lieu, "quebec")
        self.assertEqual(match.arbitre.nom, "peres")
        self.assertEqual(match.infoMatch(), "barca VS real au quebec")
        # < Communication entre les classes Match et Arbitre: Effet de la méthode matchTerminer() de la classe arbitre >
        self.assertEqual(match.arbitre.credit, 1)
        self.assertEqual(match.vainqueur.nombreDeVictoires, 1)
        self.assertEqual(match.vainqueur.nombreDePoints, 3)
        self.assertEqual(match.vaincu.nombreDeDefaites, 1)




if __name__ == '__main__':
    unittest.main()
