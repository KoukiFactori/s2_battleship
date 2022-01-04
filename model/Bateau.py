# Bateau.py

#
# - Définit un bateau sous forme de dictionnaire de la façon suivante :
#   const.BATEAU_NOM : Nom du bateau (voir les constantes dans Constantes.py - clés du dictionnaire const.BATEAUX_CASES)
#   const.BATEAU_SEGMENTS - Liste de listes [coordonnées, état] des segments du bateau.
#       Si le bateau n'est pas positionné, les coordonnées valent None et les états valent const.RATE
#   La taille du bateau n'est pas stockée car elle correspond à la taille de la liste des listes [coordonnées, état]
#

from model.Segment import type_segment, construireSegment
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
        if not (0 <= n < len(bateau[const.BATEAU_SEGMENTS])):
            raise ValueError(f"getSegmentBateau (index): Impossible d'accéder à ce segment, la valeur est en dehors des limites")

    elif type(n) == tuple:
        #Renvoie les positions de chaque segment du bateau
        segment_positions = list(map(lambda s: s[const.SEGMENT_COORDONNEES], bateau[const.BATEAU_SEGMENTS]))
        
        if n not in segment_positions:
            raise ValueError(f"getSegmentBateau (coordonnées): Impossible d'accéder à ce segment, ce segment n'existe pas sur ce bateau")
    else:
        raise ValueError(f"Le type du second paramètre {type(n)} ne correspond pas...") 

    return bateau[const.BATEAU_SEGMENTS][n if type(n) == int else segment_positions.index(n)]

def setSegmentBateau(bateau: dict, n, segment: dict):
    if not type_bateau(bateau):
        raise ValueError(f"setSegmentBateau : L'argument {bateau} n'est pas un bateau valide")
    if not type_segment(segment):
        raise ValueError(f"setSegmentBateau : L'argument {segment} n'est pas un segment valide")
    if not (0 <= n < len(bateau[const.BATEAU_SEGMENTS])):
            raise ValueError(f"getSegmentBateau : Impossible d'accéder à ce segment, la valeur est en dehors des limites")

    bateau[const.BATEAU_SEGMENTS][n] = segment

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


