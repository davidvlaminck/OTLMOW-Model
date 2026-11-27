# coding=utf-8
from typing import ClassVar

from ...BaseClasses.NonNegIntegerField import NonNegIntegerField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Oplegrij(AIMNaamObject, LijnGeometrie):
    """Een rij van opleggingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VoorzieningNegatieveReactie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderlandhoofd', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kelderpijler', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokercomplex', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Landhoofd', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pijler', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._aantalOpleggingenOpRij = OTLAttribuut(field=NonNegIntegerField,
                                                    naam='aantalOpleggingenOpRij',
                                                    label='aantal opleggingen op rij',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij.aantalOpleggingenOpRij',
                                                    definition='Het aantal opleggingen die op een rij liggen.',
                                                    owner=self)

    @property
    def aantalOpleggingenOpRij(self) -> int:
        """Het aantal opleggingen die op een rij liggen."""
        return self._aantalOpleggingenOpRij.get_waarde()

    @aantalOpleggingenOpRij.setter
    def aantalOpleggingenOpRij(self, value):
        self._aantalOpleggingenOpRij.set_waarde(value, owner=self)
