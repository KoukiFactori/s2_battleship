# Joueur.py

from model.Bateau import type_bateau, construireBateau
from model.Grille import type_grille, construireGrille
from model.Constantes import *

#
# Un joueur est représenté par un dictionnaire contenant les couples (clé, valeur) suivants :
#  const.JOUEUR_NOM : Nom du joueur de type str
#  const.JOUEUR_LISTE_BATEAUX : Liste des bateaux du joueur
#  const.JOUEUR_GRILLE_TIRS : Grille des tirs sur les bateaux adverses
#  const.JOUEUR_GRILLE_ADVERSAIRE : une grille des tirs de l'adversaire pour tester la fonction de tir
#  de l'adversaire.
#

def construireJoueur(name: str, shipsName: [str]) -> dict:
    joueur = {
        const.JOUEUR_NOM: name,
        const.JOUEUR_LISTE_BATEAUX:  [construireBateau(ship) for ship in shipsName],
        const.JOUEUR_GRILLE_TIRS: construireGrille(),
        const.JOUEUR_GRILLE_ADVERSAIRE: construireGrille()
    }

    return joueur

def getNomJoueur(joueur: dict) -> str:
    if not type_joueur(joueur):
        raise ValueError("getNomJoueur : Structure invalide, n'est pas un joueur")

    return joueur[const.JOUEUR_NOM]

def getNombreBateauxJoueur(joueur: dict) -> int:
    if not type_joueur(joueur):
        raise ValueError("getNombreBateauxJoueur : Structure invalide, n'est pas un joueur")

    return len(joueur[const.JOUEUR_LISTE_BATEAUX])

def getBateauxJoueur(joueur: dict) -> list:
    if not type_joueur(joueur):
        raise ValueError("getBateauxJoueur : Structure invalide, n'est pas un joueur")

    return joueur[const.JOUEUR_LISTE_BATEAUX]

def getGrilleTirsJoueur(joueur: dict) -> list:
    if not type_joueur(joueur):
        raise ValueError("getGrilleTirsJoueur : Structure invalide, n'est pas un joueur")

    return joueur[const.JOUEUR_GRILLE_TIRS]


def getGrilleTirsAdversaire(joueur: dict) -> list:
    if not type_joueur(joueur):
        raise ValueError("getGrilleTirsAdversaire : Structure invalide, n'est pas un joueur")

    return joueur[const.JOUEUR_GRILLE_ADVERSAIRE]

def type_joueur(joueur: dict) -> bool:
    """
    Retourne <code>True</code> si la liste semble correspondre à un joueur,
    <code>false</code> sinon.

    :param joueur: Dictionnaire représentant un joueur
    :return: <code>True</code> si le dictionnaire représente un joueur, <code>False</code> sinon.
    """
    return type(joueur) == dict and len(joueur) >= 4 and \
        len([p for p in [ const.JOUEUR_NOM, const.JOUEUR_LISTE_BATEAUX, const.JOUEUR_GRILLE_TIRS] if p not in joueur]) == 0 and \
        type(joueur[const.JOUEUR_NOM]) == str and type(joueur[const.JOUEUR_LISTE_BATEAUX]) == list \
        and type_grille(joueur[const.JOUEUR_GRILLE_TIRS]) \
        and all(type_bateau(v) for v in joueur[const.JOUEUR_LISTE_BATEAUX])


