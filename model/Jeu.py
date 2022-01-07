# model/Jeu.py

#
#  Module mettant en place les joueurs
#
from model.Joueur import estPerdantJoueur, getNomJoueur, repondreTirJoueur, type_joueur
from model.Constantes import *
from view import window
from random import choice

import pygame
from time import sleep
# Pour jouer, un joueur doit être capable de :
# - placer ses bateaux
# - choisir une case pour tirer
# - traiter le résultat d'un tir
# Pour cela, on crée un acteur : dictionnaire
#       const.ACTEUR : Joueur (voir construireJoueur)
#       const.ACTEUR_PLACER_BATEAUX : fonction permettant de placer les bateaux
#       const.ACTEUR_CHOISIR_CASE : fonction permettant de choisir la case où le tir aura lieu
#       const.ACTEUR_TRAITER_RESULTAT : fonction permettant de traiter le résultat d'un précédent tir

def jouerJeu(acteur1: dict, acteur2: dict) -> None:
    if not type_acteur(acteur1):
        raise ValueError(f"jouerJeu : L'acteur {acteur1} n'est pas valide ?")
    if not type_acteur(acteur2):
        raise ValueError(f"jouerJeu : L'acteur {acteur2} n'est pas valide, essayez de trouver un ami pour jouer quand même...")

    acteur1[const.ACTEUR_PLACER_BATEAUX](acteur1[const.ACTEUR])
    acteur2[const.ACTEUR_PLACER_BATEAUX](acteur2[const.ACTEUR])

    actual_player = choice([acteur1, acteur2])
    enemy = acteur1 if actual_player == acteur2 else acteur2

    while (not estPerdantJoueur(acteur1[const.ACTEUR])) and (not estPerdantJoueur(acteur2[const.ACTEUR])):
        window.afficher(actual_player[const.ACTEUR])
        #window.display_message(f"C'est au tour de {getNomJoueur(actual_player[const.ACTEUR])}")
        
        target = actual_player[const.ACTEUR_CHOISIR_CASE](actual_player)
        res = repondreTirJoueur(enemy[const.ACTEUR], target)
        actual_player[const.ACTEUR_TRAITER_RESULTAT](actual_player, target, res)
        
        window.refresh()
        pygame.time.delay(5)
        #window.display_message(f"Tir en {target} : {res}")
        actual_player, enemy = enemy, actual_player

    window.display_message(f"Le gagnant est {getNomJoueur(enemy[const.ACTEUR])}") #Car on a switch de joueur juste avant
    return None

def getListeBateaux() -> None:
    return [const.PORTE_AVION, const.CUIRASSE, const.CROISEUR, const.CROISEUR, const.TORPILLEUR]

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


