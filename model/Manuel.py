# model/Manuel.py
#

from view import window
from model.Joueur import getNomJoueur, type_joueur

def placerBateauxManuel(joueur: dict) -> None:

  if not type_joueur(joueur):
    raise ValueError("placerBateauxManuel : Le joueur {joueur} n'est pas un joueur valide")

  window.afficher(joueur)
  window.display_message(f"{getNomJoueur(joueur)} : Placez vos bateaux")
  window.placer_bateaux()

  return None

def choisirCaseTireManuel(joueur: dict) -> tuple:
  if not type_joueur(joueur):
    raise ValueError("choisirCaseTirManuel : Le joueur {joueur} n'est pas un joueur valide")

  window.afficher(joueur)
  window.display_message(f"{getNomJoueur(joueur)} : Choisissez la case où vous voulez tirer")
  window.set_action("Choisissez la case de tir (bouton gauche)")

  res = window.get_clicked_cell(2)
  return res