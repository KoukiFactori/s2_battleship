# Grille.py

from model.Constantes import *
from model.Case import type_case
from model.Coordonnees import type_coordonnees

#
# - Définition de la grille des tirs
#       - tableau 2D (const.DIM x const.DIM) contenant des cases de type type_case.
#
# Bien qu'on pourrait créer une autre grille contenant les bateaux, ceux-ci seront stockés dans une liste
# et chaque bateau contiendra sa liste de coordonnées.
#

def construireGrille() -> list:
    grille = []

    for rowI in range(const.DIM):
        row = []
        for colI in range(const.DIM):
            row.append(None)
        grille.append(row)
    
    return grille

def marquerCouleGrille(grille: list, coords: tuple) -> None:
    if not type_grille(grille):
        raise ValueError(f"marquerCouleGrille : La grille {grille} n'est pas une grille valide")
    if not type_coordonnees(coords):
        raise ValueError(f"marquerCouleGrille : Les coordonnées {coords} ne sont pas des coordonnées valides.")

    lst = [coords]
    while len(lst):
        el = lst.pop()
        grille[el[0]][el[1]] = const.COULE

        ff = lambda c: c[0] >= 0 and c[0] < const.DIM and c[1] >= 0 and c[1] < const.DIM and grille[c[0]][c[1]] == const.TOUCHE
        possible_moves = filter(ff, [
            (el[0] - 1, el[1]), (el[0] + 1, el[1]),
            (el[0], el[1] - 1), (el[0], el[1] + 1)
        ])

        lst.extend(possible_moves)

    
def type_grille(g: list) -> bool:
    """
    Détermine si le paramètre est une grille de cases dont le type est passé en paramètre ou non
    :param g: paramètre à tester
    :return: True s'il peut s'agir d'une grille du type voulu, False sinon.
    """
    res = True
    if type(g) != list or len(g) != const.DIM:
        res = False
    else:
        i = 0
        while res and i < len(g):
            res = type(g[i]) == list and len(g[i]) == const.DIM
            j = 0
            while res and j < len(g[i]):
                res = type_case(g[i][j])
                j += 1
            i += 1
    return res


