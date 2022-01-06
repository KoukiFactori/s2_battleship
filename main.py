import pygame

from view import window

from model.Constantes import *
from model.Joueur import construireJoueur, repondreTirJoueur
from model.Jeu import getListeBateaux, jouerJeu
from model.Manuel import placerBateauxManuel, choisirCaseTirManuel, traiterResultatTirManuel, construireActeurManuel
from model.IA import construireActeurIA

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
    a1 = construireActeurIA(construireJoueur("Teiuwu", getListeBateaux()))
    a2 = construireActeurIA(construireJoueur("Didiruwu", getListeBateaux()))
    jouerJeu(a1, a2)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()