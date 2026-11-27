# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.ElektrischComponentennummerObject import (
    ElektrischComponentennummerObject,
)
from ...Classes.Abstracten.MotorVermogenskring import MotorVermogenskring
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Werkschakelaar(ElektrischComponentennummerObject, MotorVermogenskring, SerienummerObject, AIMNaamObject):
    """Een handbediende schakelaar die in de nabijheid van een elektromechanische installatie is aangebracht om deze gedurende onderhouds- en reparatiewerkzaamheden te kunnen uitschakelen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Werkschakelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Elektromotor', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderstel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomphuis', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#MotorVermogenskring', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
