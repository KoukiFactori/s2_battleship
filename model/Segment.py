# model/Segment.py

from model.Coordonnees import type_coordonnees
from model.Etat import type_etat_segment
from model.Constantes import *

#
# définit un segment de bateau :
# Un segment de bateau est un dictionnaire contenant les couples (clé, valeur) suivants :
#   - const.SEGMENT_COORDONNEES : Les coordonnées du segment sur la grille
#   - const.SEGMENT_ETAT : L'état du segment (const.INTACT ou const.TOUCHE)
#

def construireSegment(coords: [int, int] = None):
    if not type_coordonnees(coords):
        raise ValueError(f"construireSegment : le paramètre {coords} ne correspond pas à des coordonnées")

    segment = {
        const.SEGMENT_COORDONNEES: coords,
        const.SEGMENT_ETAT: const.INTACT
    }

    return segment

def getCoordonneesSegment(segment: dict) -> [int, int]:
    if not type_segment(segment):
        raise ValueError(f"getCoordonneesSegment : le paramètre {segment} n'est pas de type Segment.")
    
    return segment[const.SEGMENT_COORDONNEES]

def getEtatSegment(segment: dict) -> str:
    if not type_segment(segment):
        raise ValueError(f"getEtatSegment : le paramètre {segment} n'est pas de type Segment.")

    return segment[const.SEGMENT_ETAT]

def setCoordonneesSegment(segment: dict, coords: [int, int]) -> None:
    if not type_segment(segment):
        raise ValueError(f"setCoordonneesSegment : le paramère {segment} n'est pas de type Segment.")
    
    if not type_coordonnees(coords):
        raise ValueError(f"setCoordonneesSegment : le paramètre {coords} n'est pas de type coordonnées")

    segment[const.SEGMENT_COORDONNEES] = coords

def setEtatSegment(segment: dict, etat: str) -> None:
    if not type_segment(segment):
        raise ValueError(f"setEtatSegment : le paramère {segment} n'est pas de type Segment.")

    if not type_etat_segment(etat):
        raise ValueError(f"setEtatSegment : le paramètre {etat} n'est pas de type Etat")

    segment[const.SEGMENT_ETAT] = etat

def type_segment(objet: dict) -> bool:

    """
    Détermine si l'objet passé en paramètre peut être interprété ou non
    comme un segment de bateau.

    :param objet: Objet à analyser
    :return: True si l'objet peut correspondre à un segment
    False sinon.
    """
    return type(objet) == dict and \
           all([k in objet for k in [const.SEGMENT_COORDONNEES, const.SEGMENT_ETAT]]) \
           and type_coordonnees(objet[const.SEGMENT_COORDONNEES]) \
           and type_etat_segment(objet[const.SEGMENT_ETAT])
