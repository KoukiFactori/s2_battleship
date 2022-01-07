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
  print(f"> {getNomJoueur(acteur[const.ACTEUR])}\n")
  if not acteur[const.TARGETING_SPECIFIC_SHIP]:
    grid = getGrilleTirsJoueur(acteur[const.ACTEUR])
    
    #ToDo: pick directly an available position instead of just guessing one
    res = (randint(0, const.DIM - 1), randint(0, const.DIM - 1))
    while grid[res[0]][res[1]] != None:
      res = (randint(0, const.DIM - 1), randint(0, const.DIM - 1))
    print("Je tire au hasard")
  else:
    base_cell = acteur[const.TARGET_SESSION][const.BASE_HIT_SUCCESSFUL]
    hit_direction = acteur[const.TARGET_SESSION][const.HIT_DIRECTION]
    print(base_cell, hit_direction)
    res = (base_cell[0] + hit_direction[0], base_cell[1] + hit_direction[1])
  print("J'ai tiré en", res)
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
    acteur[const.TARGETING_SPECIFIC_SHIP] = False
    acteur[const.TARGET_SESSION] = reinitialiserSession()
    print("Bateau coulé ! Je réinitialise la session")
    print("----------------------------------------")
  elif res == const.TOUCHE:
    print("Bateau touché")
    
    session = acteur[const.TARGET_SESSION]
    if not acteur[const.TARGETING_SPECIFIC_SHIP]:
      acteur[const.TARGETING_SPECIFIC_SHIP] = True
      session[const.SHIP_HIT_POSITIONS].append(coords)

      #hit_direction is (0, 0)
      target_direction = change_hit_direction(session[const.HIT_DIRECTION], 1)
      #calc the next position
      next_position = (coords[0] + target_direction[0], coords[1] + target_direction[1])
      #if the next position is OOB, change the direction until a valid one
      while not type_coordonnees(next_position):
        target_direction = change_hit_direction(target_direction, 1)
        next_position = (coords[0] + target_direction[0], coords[1] + target_direction[1])

      if target_direction is None:
        print("Not in a session, but no direction is valid, ending code")
        raise RuntimeError("No direction available")
      else:
        session[const.HIT_DIRECTION] = target_direction
        session[const.BASE_HIT_SUCCESSFUL] = coords
        print("Je ne visais pas de bateau avant, session démarrée : ", session)
    else: #In a session, can only happen when 2 hits are made to the ship
      session[const.SHIP_HIT_POSITIONS].append(coords)
      
      x = session[const.HIT_DIRECTION]
      next_position = (coords[0] + x[0], coords[1] + x[1])
      if not type_coordonnees(next_position): #if the next position is invalid, should take the other end
        session[const.BASE_HIT_SUCCESSFUL] = session[const.SHIP_HIT_POSITIONS][0] #Restart from the first segment good
        session[const.HIT_DIRECTION] = change_hit_direction(session[const.HIT_DIRECTION], 1) #And turn back
      else:
        #Keep the direction until a miss
        session[const.BASE_HIT_SUCCESSFUL] = coords
    print("----------------------------------------")
  else: #const.FAIL
    print("Echec du tir")
    session = acteur[const.TARGET_SESSION]
    if acteur[const.TARGETING_SPECIFIC_SHIP]:
      if len(session[const.SHIP_HIT_POSITIONS]) == 1: #if we aren't sure of the orientation of the ship

        #absolute bullshit, where are the reel coords? 

        x = change_hit_direction(session[const.HIT_DIRECTION], 1)
        next_position = (coords[0] + x[0], coords[1] + x[1])
        while type_coordonnees(next_position) == False:
          x = change_hit_direction(x, 1)
          next_position = (coords[0] + x[0], coords[1] + x[1])
      
        if x is None: #For some reasons, no segment is around... weird
          acteur[const.TARGETING_SPECIFIC_SHIP] = False
          acteur[const.TARGET_SESSION] = reinitialiserSession()
        else:
          session[const.HIT_DIRECTION] = x
      else: #Already have the direction of the ship, just go back to hit the other end
        session[const.BASE_HIT_SUCCESSFUL] = session[const.SHIP_HIT_POSITIONS][0] #Restart from the first segment good
        session[const.HIT_DIRECTION] = change_hit_direction(session[const.HIT_DIRECTION], 1) #And turn back
    print("----------------------------------------")
  return None

def change_hit_direction(direction, t):
  hit_directions = [
    (0, 0), #Stand-by
    (-1, 0), (1, 0), #Vertical axis checking
    (0, -1), (0, 1) #Horizontal axis checking
  ]
  x = hit_directions.index(direction) + t
  if x >= len(hit_directions):
    return None
  else:
    return hit_directions[x]

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
      const.SHIP_HIT_POSITIONS: [], #tracking positions based on time
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