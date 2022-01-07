# model/IA.py
from view import window
from random import randint

from model.Joueur import type_joueur, getGrilleTirsJoueur, getNomJoueur
from model.Constantes import *
from model.Grille import marquerCouleGrille
from model.Coordonnees import type_coordonnees
from model.Etat import lst_resultat_tir
from model.Jeu import type_acteur

def placerBateauxIA(joueur: dict) -> None:
  window.afficher(joueur)
  window.display_message(f"{getNomJoueur(joueur)} : Placez vos bateaux")
  window.placer_bateaux()
  return None

def choisirCaseTirIA(acteur: dict) -> tuple: #Appelé à chaque fois que l'IA doit tirer
  if not type_acteur(acteur):
    raise ValueError(f"choisirCaseTirIA : L'acteur {acteur} n'est pas un acteur valide")
  window.afficher(acteur[const.ACTEUR])

  if not acteur[const.TARGETING_SPECIFIC_SHIP]:
    grid = getGrilleTirsJoueur(acteur[const.ACTEUR])
    
    #ToDo: pick directly an available position instead of just guessing one
    res = (randint(0, const.DIM - 1), randint(0, const.DIM - 1))
    while grid[res[0]][res[1]] != None:
      res = (randint(0, const.DIM - 1), randint(0, const.DIM - 1))
  else:
    base_cell = acteur[const.TARGET_SESSION][const.BASE_HIT_SUCCESSFUL]
    hit_direction = acteur[const.TARGET_SESSION][const.HIT_DIRECTION]
    res = (base_cell[0] + hit_direction[0], base_cell[1] + hit_direction[0])
  return res

def traiterResultatTirIA(acteur: dict, coords: tuple, res: str) -> None:
  #Donne le résultat du tir à l'IA ainsi que le position
  if not type_acteur(acteur):
    raise ValueError(f"traiterResultatTirIA : L'acteur {acteur} n'est pas un acteur valide")
  if not type_coordonnees(coords) or coords is None:
    raise ValueError(f"traiterResultatTirIA : Les coordonnées {coords} ne sont pas des coordonnées valides ou non nulles")
  if res not in lst_resultat_tir:
    raise ValueError(f"traiterResultatTirIA : La réponse {res} reçue ne ressemble pas à un résultat de tir.")

  grid = getGrilleTirsJoueur(acteur[const.ACTEUR])
  grid[coords[0]][coords[1]] = res

  if res == const.COULE:
    marquerCouleGrille(grid, coords)
    acteur[const.TARGET_SESSION] = reinitialiserSession()
  else: #res == const.RATE
    pass

  return None

def construireActeurIA(joueur: dict) -> dict:
  if not type_joueur(joueur):
    raise ValueError(f"construireActeurIA : Je sais bien qu'on essaye de faire un faux joueur, mais {joueur} n'est pas un joueur valide.")
  
  return {
    const.ACTEUR: joueur,
    const.ACTEUR_PLACER_BATEAUX: placerBateauxIA,
    const.ACTEUR_CHOISIR_CASE: choisirCaseTirIA,
    const.ACTEUR_TRAITER_RESULTAT: traiterResultatTirIA,
    
    #IA specific variables
    const.TARGETING_SPECIFIC_SHIP: False,
    const.TARGET_SESSION: {
      const.SHIP_HIT_POSITIONS: [],
      const.HIT_DIRECTION: (0, 0),
      const.BASE_HIT_SUCCESSFUL: (0, 0)
    }
  }

def reinitialiserSession() -> dict:
  return {
    const.SHIP_HIT_POSITIONS: [],
    const.HIT_DIRECTION: (0, 0),
    const.BASE_HIT_SUCCESSFUL: (0, 0)
  }