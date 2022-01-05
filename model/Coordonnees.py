# Coordonnees.py


#
# - Définit les coordonnées d'une case
#
#  Une coordonnée est un tuple de deux entiers compris entre 0 (inclus) et const.DIM (exclus)
#  Elle peut aussi être None si elle est non définie
#


from model.Constantes import *


def sontVoisins(first_pos: tuple, other_pos: tuple) -> bool:

    if not type_coordonnees(first_pos) or first_pos is None:
        raise ValueError(f"sontVoisins : La coordonnée {first_pos} n'est pas valide")

    if not type_coordonnees(other_pos) or other_pos is None:
        raise ValueError(f"sontVoisins : La coordonnée {other_pos} n'est pas valide")

    v_diff = (first_pos[0] - other_pos[0])
    h_diff = (first_pos[1] - other_pos[1])

    return 0 < v_diff**2 + h_diff**2 <= 2

def type_coordonnees(c: tuple) -> bool:
    """

    Détermine si le tuple correspond à des coordonnées

    Les coordonnées sont sous la forme (ligne, colonne).

    Malheureusement, il n'est pas possible de tester si une inversion est faite entre ligne et colonne...


    :param c: coordonnées

    :return: True s'il s'agit bien de coordonnées, False sinon
    """

    return c is None or (type(c) == tuple and len(c) == 2 and 0 <= c[0] < const.DIM and 0 <= c[1] < const.DIM)
