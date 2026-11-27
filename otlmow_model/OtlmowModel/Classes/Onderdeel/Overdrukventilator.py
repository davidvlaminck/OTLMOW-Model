# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.Ventilatie import Ventilatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Overdrukventilator(Ventilatie):
    """Onderdeel dat tot doel heeft overdruk te creëren in een gesloten ruimte zodat bij het openen van de ruimte enkel lucht kan ontsnappen naar buiten en geen lucht,rook,partikels,... naar binnen te laten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overdrukventilator'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
