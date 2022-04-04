from partie_2.championnat.organisation.championnat import Championnat
from partie_2.championnat.personnel.arbitre import Arbitre
from partie_2.championnat.personnel.joueur import Joueur
from partie_2.championnat.personnel.staff import Staff
from partie_2.championnat.organisation.equipe import Equipe
from partie_2.championnat.organisation.match import Match


# Creer un nouveau championnat
liga = Championnat("Liga", "Espagne")

# Creer deux joueurs
messi = Joueur("messi", "lionnel", 34, "attaquant", 10)
ronaldo = Joueur("cristiano", "ronaldo", 35, "attaquant", 7)

# Creer deux equipes
barca = Equipe("barca")
real = Equipe("real")

# Accepter les joueurs dans des equipes
barca.ajoutJoueur(messi)
real.ajoutJoueur(ronaldo)

# Creer des staff (membre de l'organisation) pour les equipes
staff_barca = Staff("lo", "khadim", 67)
staff_real = Staff("alian", "giresse", 65)

# creer un arbitre
arbitre = Arbitre("monsieur", "l'arbitre", 45)

# Inscrire les equipes dans le championnat
liga.ajoutEquipe(barca)
liga.ajoutEquipe(real)

# Organiser un match entre deux equipes
match = Match(barca, real)

# Ajouter le match dans le programme du championnat
liga.ajoutMatch(match)

print("---------------Real avant match-----------------")

staff_real.doonerRole("adjoint")
barca.recruter(staff_real)
staff_real.infoStaff()
real.infosEquipe()

print("--------------Barca avant match-----------------")

staff_barca.doonerRole("entraineur")
barca.recruter(staff_barca)
staff_barca.infoStaff()
barca.infosEquipe()


arbitre.affectation("central")

print("-------------Deroulement du match----------------")

match.ajouArbitre(arbitre)
match.ajoutLieu("quebec")
match.ajoutDate("le 24 decembre")
match.infoMatch()
arbitre.matchTerminer(barca, real, 2, 4)

print("--------------------Apres match------------------")
print("---------------barca apres match-----------------")
barca.infosEquipe()
print("--------------real apres match-------------------")
real.infosEquipe()

print("-------------------classement--------------------")

liga.classement()
barca.infosEquipe()
real.infosEquipe()
messi.donnerJaune()
messi.donnerJaune()
messi.marquerBut()

print("-------------------Information de Messi--------------------")
print(messi.infoJoueur())

print("-------------------Information staff de barca--------------------")
print(staff_barca.infoStaff())

print("-------------------Information arbitre--------------------")
print(arbitre.infoArbitre())

