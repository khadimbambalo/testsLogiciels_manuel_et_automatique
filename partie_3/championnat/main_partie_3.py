from partie_3.championnat.organisation.championnat import Championnat
from partie_3.championnat.personnel.arbitre import Arbitre
from partie_3.championnat.personnel.joueur import Joueur
from partie_3.championnat.personnel.staff import Staff
from partie_3.championnat.organisation.equipe import Equipe
from partie_3.championnat.organisation.match import Match


# Creer un nouveau championnat
liga = Championnat("Liga", "Espagne")

# Creer deux joueurs
messi = Joueur("messi", "lionnel", 34, "attaquant", 10)
ronaldo = Joueur("cristiano", "ronaldo", 35, "attaquant", 7)

# Creer deux equipes
barca = Equipe("barca")
real = Equipe("real")
chelsea = Equipe("chelsea")
paris = Equipe("paris")
arsenal = Equipe("arsenal")
marseille = Equipe("marseille")

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
liga.ajoutEquipe(chelsea)
liga.ajoutEquipe(paris)
liga.ajoutEquipe(arsenal)
liga.ajoutEquipe(marseille)

# Organiser un match entre deux equipes
match_1 = Match(barca, real)
match_2 = Match(chelsea, paris)
match_3 = Match(arsenal, marseille)
match_4 = Match(barca, paris)
match_5 = Match(arsenal, real)
match_6 = Match(marseille, chelsea)

# Ajouter le match dans le programme du championnat
liga.ajoutMatch(match_1)
liga.ajoutMatch(match_2)
liga.ajoutMatch(match_3)
liga.ajoutMatch(match_4)
liga.ajoutMatch(match_5)
liga.ajoutMatch(match_6)

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

match_1.ajouArbitre(arbitre)
match_1.ajoutLieu("quebec")
match_1.ajoutDate("le 23 decembre")

match_2.ajouArbitre(arbitre)
match_2.ajoutLieu("montreal")
match_2.ajoutDate("le 13 decembre")

match_3.ajouArbitre(arbitre)
match_3.ajoutLieu("chicoutimi")
match_3.ajoutDate("le 24 novembre")

match_4.ajouArbitre(arbitre)
match_4.ajoutLieu("Levis")
match_4.ajoutDate("le 24 janvier")

match_5.ajouArbitre(arbitre)
match_5.ajoutLieu("ottawa")
match_5.ajoutDate("le 04 mars")

match_6.ajouArbitre(arbitre)
match_6.ajoutLieu("ontario")
match_6.ajoutDate("le 24 avril")

print("-------------Match 1----------------")
match_1.infoMatch()
print("-------------Match 2----------------")
match_2.infoMatch()
print("-------------Match 3----------------")
match_3.infoMatch()
print("-------------Match 4----------------")
match_4.infoMatch()
print("-------------Match 5----------------")
match_5.infoMatch()
print("-------------Match 6----------------")
match_6.infoMatch()

arbitre.matchTerminer(barca, real, 2, 1)
arbitre.matchTerminer(chelsea, paris, 2, 0)
arbitre.matchTerminer(arsenal, marseille, 3, 1)
arbitre.matchTerminer(barca, paris, 3, 0)
arbitre.matchTerminer(arsenal, real, 0, 0)
arbitre.matchTerminer(marseille, chelsea, 2, 0)

print("--------------------Apres match------------------")
print("---------------barca apres match-----------------")
barca.infosEquipe()
print("--------------real apres match-------------------")
real.infosEquipe()
print("---------------chelsea apres match-----------------")
chelsea.infosEquipe()
print("--------------paris apres match-------------------")
paris.infosEquipe()
print("---------------arsenal apres match-----------------")
arsenal.infosEquipe()
print("--------------marseille apres match-------------------")
marseille.infosEquipe()

print("-------------------classement--------------------")

liga.classement()
barca.infosEquipe()

print("-------------------Information de Messi--------------------")
real.infosEquipe()
messi.donnerJaune()
messi.donnerJaune()
messi.marquerBut()
print(messi.infoJoueur())

print("-------------------Information staff de barca--------------------")
print(staff_barca.infoStaff())

print("-------------------Information arbitre--------------------")
print(arbitre.infoArbitre())

print("-------------------Macths de la supercoupe avec les équipes sélectionnées automatiquement selon le classement--------------------")
liga.superCoupe()

# Creation des arbitres de la super coupe
arbitre_1 = Arbitre("monsieur_super_coupe", "l'arbitre_1", 34)
arbitre_2 = Arbitre("monsieur_super_coupe", "l'arbitre_2", 45)
liga.super_coupe.match_1.ajouArbitre(arbitre_1)
liga.super_coupe.match_2.ajouArbitre(arbitre_2)
print(liga.super_coupe.match_1.arbitre.infoArbitre())
