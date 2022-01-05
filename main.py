import pygame

from view import window

from model.Constantes import *
from model.Joueur import construireJoueur

from model.Manuel import placerBateauxManuel

def main_test():
    j = construireJoueur("Teiuwu", [const.PORTE_AVION, const.CUIRASSE, const.CROISEUR, const.TORPILLEUR])
    # j = construireJoueur("Test", [const.PORTE_AVION, const.CUIRASSE])
    
    placerBateauxManuel(j)
    window.set_action("Pour terminer, cliquez dans la grille de DROITE")
    window.get_clicked_cell(2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_test()