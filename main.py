import pygame

from view import window

from model.Constantes import *
from model.Joueur import construireJoueur, repondreTirJoueur
from model.Jeu import getListeBateaux, jouerJeu
from model.Manuel import placerBateauxManuel, choisirCaseTirManuel, traiterResultatTirManuel

def main_test():
    #j = construireJoueur("Teiuwu", [const.PORTE_AVION, const.CUIRASSE, const.CROISEUR, const.TORPILLEUR])
    j = construireJoueur("Teiuwu", [const.PORTE_AVION, const.CUIRASSE])
    
    placerBateauxManuel(j)
    window.set_action("Pour terminer, cliquez dans la grille de DROITE")
    window.get_clicked_cell(2)
    while True:
        x = choisirCaseTirManuel(j)
        res = repondreTirJoueur(j, x)
        traiterResultatTirManuel(j, x, res)
        window.refresh()
    window.set_action("Pour terminer, cliquez dans la grille de DROITE") 
    window.get_clicked_cell(2)

def main():
    j1 = construireJoueur("Teiuwu", getListeBateaux())
    j2 = construireJoueur("Didiruwu", getListeBateaux())
    jouerJeu(j1, j2)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()