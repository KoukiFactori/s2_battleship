# model/Manuel.py
#

from view import window
from model.Joueur import getNomJoueur, type_joueur, getGrilleTirsJoueur
from model.Constantes import *
from model.Grille import type_grille, marquerCouleGrille
from model.Coordonnees import type_coordonnees
from model.Etat import lst_resultat_tir


def placerBateauxManuel(joueur: dict) -> None:

  if not type_joueur(joueur):
    raise ValueError(f"placerBateauxManuel : Le joueur {joueur} n'est pas un joueur valide")

  window.afficher(joueur)
  window.display_message(f"{getNomJoueur(joueur)} : Placez vos bateaux")
  window.placer_bateaux()

  return None

def choisirCaseTirManuel(joueur: dict) -> tuple:
  if not type_joueur(joueur):
    raise ValueError(f"choisirCaseTirManuel : Le joueur {joueur} n'est pas un joueur valide")

  window.afficher(joueur)
  #window.display_message(f"{getNomJoueur(joueur)} : Choisissez la case où vous voulez tirer")
  window.set_action("Choisissez la case de tir (bouton gauche)")

  res = window.get_clicked_cell(2)
  return res[0]

def traiterResultatTirManuel(joueur: dict, coords: tuple, res: str) -> None:
  if not type_joueur(joueur):
    raise ValueError(f"traiterResultatTirManuel : Le joueur {joueur} n'est pas un joueur valide")
  if not type_coordonnees(coords) or coords is None:
    raise ValueError(f"traiterResultatTirManuel : Les coordonnées {coords} ne sont pas des coordonnées valides ou non nulles")
  if res not in lst_resultat_tir:
    raise ValueError(f"traiterResultatTriManuel : La réponse {res} reçue ne ressemble pas à un résultat de tir.")

  grid = getGrilleTirsJoueur(joueur)
  grid[coords[0]][coords[1]] = res
  if res == const.COULE:
    marquerCouleGrille(grid, coords)

  return None