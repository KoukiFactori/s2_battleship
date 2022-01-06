# model/IA.py
from view import window
from model.Joueur import getNomJoueur, type_joueur, getGrilleTirsJoueur
from model.Constantes import *
from model.Grille import type_grille, marquerCouleGrille
from model.Coordonnees import type_coordonnees
from model.Etat import lst_resultat_tir
from random import randint

def placerBateauxIA(joueur: dict) -> None:

  window.afficher(joueur)
  window.display_message(f"{getNomJoueur(joueur)} : Placez vos bateaux")
  window.placer_bateaux()

  return None

def choisirCaseTirIA(joueur: dict) -> tuple: #Appelé à chaque fois que l'IA doit tirer
  if not type_joueur(joueur):
    raise ValueError(f"choisirCaseTirManuel : Le joueur {joueur} n'est pas un joueur valide")

  window.afficher(joueur)
  #window.display_message(f"{getNomJoueur(joueur)} : Choisissez la case où vous voulez tirer")
  window.set_action("Choisissez la case de tir (bouton gauche)")

  res = (randint(0, const.DIM - 1), randint(0, const.DIM - 1))
  return res

def traiterResultatTirIA(joueur: dict, coords: tuple, res: str) -> None:
  #Donne le résultat du tir à l'IA ainsi que le position
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

"""
{
  
}

if not targeting_specific_ship:
  #tir random
else:
  target_cell = (base_cell[0] + hit_direction[0], base_cell[1] + hit_direction[0])
  choisirCaseTirIA(target_cell)
  if reponseTirIA == const.COULE:
    targeting_specific_ship = False
    current_ship_hit_position = []
    hit_direction = (0, 0)
    last_hit_succesful = (0, 0)
"""


def construireActeurIA(joueur: dict) -> dict:
  if not type_joueur(joueur):
    raise ValueError(f"construireActeurManuel : Je sais bien qu'on essaye de faire un faux joueur, mais {joueur} n'est pas un joueur valide.")
  
  return {
    const.ACTEUR: joueur,
    const.ACTEUR_PLACER_BATEAUX: placerBateauxIA,
    const.ACTEUR_CHOISIR_CASE: choisirCaseTirIA,
    const.ACTEUR_TRAITER_RESULTAT: traiterResultatTirIA,
    
    #IA specific variables
    const.TARGETING_SPECIFIC_SHIP: True,
    #"current_ship_hit_positions": [],
    #"hit_direction": (0, 1), # (up/no/down, left/no/right)
    #"last_hit_succesful": (y, x)
  }