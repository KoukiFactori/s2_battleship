# model/Jeu.py

#
#  Module mettant en place les joueurs
#
from model.Joueur import type_joueur, estPerdantJoueur, getNomJoueur
from model.Constantes import *
from view import window
from random import choice
from model.Manuel import *
# Pour jouer, un joueur doit être capable de :
# - placer ses bateaux
# - choisir une case pour tirer
# - traiter le résultat d'un tir
# Pour cela, on crée un acteur : dictionnaire
#       const.ACTEUR : Joueur (voir construireJoueur)
#       const.ACTEUR_PLACER_BATEAUX : fonction permettant de placer les bateaux
#       const.ACTEUR_CHOISIR_CASE : fonction permettant de choisir la case où le tir aura lieu
#       const.ACTEUR_TRAITER_RESULTAT : fonction permettant de traiter le résultat d'un précédent tir

def jouerJeu(player1: dict, player2: dict) -> None:
    if not type_joueur(player1):
        raise ValueError(f"jouerJeu : Le joueur {player1} n'est pas valide, essayez de jouer contre un arbre ?")
    if not type_joueur(player2):
        raise ValueError(f"jouerJeu : Le joueur {player2} n'est pas valide, essayez de trouver un ami pour jouer quand mê   me...")

    placerBateauxManuel(player1)
    placerBateauxManuel(player2)

    actual_player = choice([player1, player2])
    switch_player = lambda: player2 if actual_player == player1 else player1

    while (not estPerdantJoueur(player1)) or (not estPerdantJoueur(player2)):
        window.afficher(actual_player)
        window.display_message(f"C'est au tour de {getNomJoueur(actual_player)}")
        
        x = choisirCaseTirManuel(actual_player)
        res = repondreTirJoueur(actual_player, x)
        traiterResultatTirManuel(actual_player, x, res)
        
        window.refresh()
        window.display_message(f"Tir en {x} : {res}")
        
        switch_player()
    return None



def type_acteur(agent: dict) -> bool:
    """
    Détermine si le tuple passé en paramètre peut être un agent ou non
    :param agent: Agent à tester
    :return: True si c'est un agent, False sinon
    """
    return type(agent) == dict and \
        all(k in agent for k in [const.ACTEUR,
                                 const.ACTEUR_PLACER_BATEAUX,
                                 const.ACTEUR_CHOISIR_CASE,
                                 const.ACTEUR_TRAITER_RESULTAT]) and \
        type_joueur(agent[const.ACTEUR]) and \
        callable(agent[const.ACTEUR_PLACER_BATEAUX]) and callable(agent[const.ACTEUR_CHOISIR_CASE]) and \
        callable(agent[const.ACTEUR_TRAITER_RESULTAT])


