# Bateau.py

#
# - Définit un bateau sous forme de dictionnaire de la façon suivante :
#   const.BATEAU_NOM : Nom du bateau (voir les constantes dans Constantes.py - clés du dictionnaire const.BATEAUX_CASES)
#   const.BATEAU_SEGMENTS - Liste de listes [coordonnées, état] des segments du bateau.
#       Si le bateau n'est pas positionné, les coordonnées valent None et les états valent const.RATE
#   La taille du bateau n'est pas stockée car elle correspond à la taille de la liste des listes [coordonnées, état]
#

from model.Coordonnees import type_coordonnees, sontVoisins
from model.Segment import type_segment, construireSegment, getCoordonneesSegment, setCoordonneesSegment
from model.Constantes import *

def construireBateau(name: str) -> dict:
    if name not in const.BATEAUX_CASES.keys():
        raise ValueError("Nom de bateau invalide")
    
    seg_nb = const.BATEAUX_CASES[name]

    bateau = {
        const.BATEAU_NOM: name,
        const.BATEAU_SEGMENTS: [construireSegment() for segment in range(seg_nb)]
    }

    return bateau

def getNomBateau(bateau: dict) -> str:

    if not type_bateau(bateau):
        raise ValueError(f"getNomBateau : L'argument {bateau} n'est pas un bateau valide")

    return bateau[const.BATEAU_NOM]

def getTailleBateau(bateau: dict) -> str:

    if not type_bateau(bateau):
        raise ValueError(f"getTailleBateau : L'argument {bateau} n'est pas un bateau valide")

    return len(bateau[const.BATEAU_SEGMENTS])

def getSegmentsBateau(bateau: dict) -> list:
    if not type_bateau(bateau):
        raise ValueError(f"getSegmentsBateau : L'argument {bateau} n'est pas un bateau valide")

    return bateau[const.BATEAU_SEGMENTS]

def getSegmentBateau(bateau: dict, n) -> dict:
    if not type_bateau(bateau):
        raise ValueError(f"getSegmentBateau : L'argument {bateau} n'est pas un bateau valide")

    if type(n) == int:
        if not (0 <= n < getTailleBateau(bateau)):
            raise ValueError(f"getSegmentBateau (index): Impossible d'accéder à ce segment, la valeur est en dehors des limites")

    elif type(n) == tuple:
        #Renvoie la position de chaque segment du bateau
        segment_positions = list(map(lambda s: s[const.SEGMENT_COORDONNEES], bateau[const.BATEAU_SEGMENTS]))
        
        if n not in segment_positions:
            raise ValueError(f"getSegmentBateau (coordonnées): Impossible d'accéder à ce segment, ce segment n'existe pas sur ce bateau")
    else:
        raise ValueError(f"Le type du second paramètre {type(n)} ne correspond pas...") 

    return bateau[const.BATEAU_SEGMENTS][n if type(n) == int else segment_positions.index(n)]

def setSegmentBateau(bateau: dict, n, segment: dict) -> None:
    if not type_bateau(bateau):
        raise ValueError(f"setSegmentBateau : L'argument {bateau} n'est pas un bateau valide")
    if not type_segment(segment):
        raise ValueError(f"setSegmentBateau : L'argument {segment} n'est pas un segment valide")
    if not 0 <= n < getTailleBateau(bateau):
            raise ValueError(f"setSegmentBateau : Impossible d'accéder à ce segment, la valeur est en dehors des limites")

    bateau[const.BATEAU_SEGMENTS][n] = segment

def getCoordonneesBateau(bateau: dict) -> list:
    if not type_bateau(bateau):
        raise ValueError(f"getCoordonneesBateau : L'argument {bateau} n'est pas un bateau valide")

    return list(map(lambda s: s[const.SEGMENT_COORDONNEES], bateau[const.BATEAU_SEGMENTS]))

def peutPlacerBateau(bateau: dict, first_case: tuple, rot_h: bool) -> bool:
    if not type_bateau(bateau):
        raise ValueError(f"peutPlacerBateau : L'argument {bateau} n'est pas un bateau valide")
    if not type_coordonnees(first_case) or first_case is None:
        raise ValueError(f"peutPlacerBateau : L'argument {first_case} n'est pas une coordonnée valide")

    ship_size = getTailleBateau(bateau)
    last_pos = (first_case[0], first_case[1] + (ship_size - 1)) if rot_h else (first_case[0] + (ship_size - 1), first_case[1])

    return type_coordonnees(last_pos)

def estPlaceBateau(bateau: dict) -> bool:
    if not type_bateau(bateau):
        raise ValueError(f"estPlaceBateau : L'argument {bateau} n'est pas un bateau valide")

    return all([*map(getCoordonneesSegment, getSegmentsBateau(bateau))])

def sontVoisinsBateau(first_ship: dict, other_ship: dict) -> bool:
    if not type_bateau(first_ship):
        raise ValueError(f"sontVoisinsBateau : L'argument {first_ship} n'est pas un bateau valide")
    if not type_bateau(other_ship):
        raise ValueError(f"sontVoisinsBateau : L'argument {other_ship} n'est pas un bateau valide")
    if not estPlaceBateau(first_ship):
        raise ValueError(f"sontVoisinsBateau : Le bateau {first_ship} n'est pas placé")
    if not estPlaceBateau(other_ship):
        raise ValueError(f"sontVoisinsBateau : Le bateau {other_ship} n'est pas placé")

    seg_coords1 = [getCoordonneesSegment(seg_first) for seg_first in getSegmentsBateau(first_ship)]
    seg_coords2 = [getCoordonneesSegment(seg_other) for seg_other in getSegmentsBateau(other_ship)]
    return any([sontVoisins(first_pos, other_pos) for first_pos in seg_coords1 for other_pos in seg_coords2])

def placerBateau(bateau: dict, first_case: tuple, is_horizontal: bool) -> None:
    if not type_bateau(bateau):
        raise ValueError(f"placerBateau : L'argument {bateau} n'est pas un bateau")

    if not type_coordonnees(first_case):
        raise ValueError(f"placerBateau : L'argument {first_case} n'est pas une coordonnées valide")

    if not peutPlacerBateau(bateau, first_case, is_horizontal):
        raise RuntimeError(f"placerBateau : Impossible de placer le bateau à ces coordonnées, sortie de plateau")

    ship_segments = getSegmentsBateau(bateau)
    taille_bateau = getTailleBateau(bateau)
    for x in range(taille_bateau):
        segment = getSegmentBateau(bateau, x)
        seg_pos = getCoordonneesSegment(segment)
        if is_horizontal:
            setCoordonneesSegment(segment, (first_case[0], first_case[1] + x))
        else:
            setCoordonneesSegment(segment, (first_case[0] + x, first_case[1]))

def type_bateau(bateau: dict) -> bool:
    """
    Détermine si la liste représente un bateau

    :param bateau: Liste représentant un bateau
    :return: <code>True</code> si la liste contient bien un bateau, <code>False</code> sinon.
    """
    return type(bateau) == dict and \
        all([v in bateau for v in [const.BATEAU_NOM, const.BATEAU_SEGMENTS]]) and \
        type(bateau[const.BATEAU_NOM]) == str and \
        bateau[const.BATEAU_NOM] in const.BATEAUX_CASES and type(bateau[const.BATEAU_SEGMENTS]) == list and \
        len(bateau[const.BATEAU_SEGMENTS]) == const.BATEAUX_CASES[bateau[const.BATEAU_NOM]] and \
        all([type_segment(s) for s in bateau[const.BATEAU_SEGMENTS]])

def est_horizontal_bateau(bateau: dict) -> bool:
    """
    Retourne True si le bateau est horizontal, False si il est vertical.

    :param bateau:
    :return: True si le bateau est horizontal, False si il est vertical
    :raise ValueError si le bateau n'est pas placé ou s'il n'est ni vertical, ni horizontal
    """
    if not estPlaceBateau(bateau):
        raise ValueError("est_horizontal_bateau: Le bateau n'est pas positionné")
    pos = getCoordonneesBateau(bateau)
    res = True
    if len(pos) > 1:
        # Horizontal : le numéro de ligne ne change pas
        res = pos[0][0] == pos[1][0]
        # On vérifie que le bateau est toujours horizontal
        for i in range(1, len(pos)):
            if (res and pos[0][0] != pos[i][0]) or (not res and pos[0][1] != pos[i][1]):
                raise ValueError("est_horizontal_bateau: Le bateau n'est ni horizontal, ni vertical ??")
    return res