# coding=utf-8
from typing import ClassVar

from ...BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class AanzichtVerkeersbordopstelling(AIMNaamObject, PuntGeometrie):
    """Een aanzicht van een verkeersbordopstelling is de verzameling van één of meerdere verkeersborden en hun bijbehorende ondersteunende elementen,zoals palen en eventuele onderborden, zoals deze zichtbaar zijn vanuit een specifieke kijkhoek of positie in de verkeerssituatie. Het aanzicht biedt inzicht in de ruimtelijke indeling, plaatsing en zichtbaarheid van de verkeersborden ten opzichte van de weggebruikers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#AanzichtVerkeersbordopstelling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanzicht', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Verkeersbordopstelling', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._foto = OTLAttribuut(field=DtcDocument,
                                  naam='foto',
                                  label='foto',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#AanzichtVerkeersbordopstelling.foto',
                                  definition='Een foto van de opstelling zoals die te zien is op het openbaar domein.',
                                  owner=self)

        self._hoek = OTLAttribuut(field=FloatOrDecimalField,
                                  naam='hoek',
                                  label='hoek',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#AanzichtVerkeersbordopstelling.hoek',
                                  usagenote='hoek',
                                  definition='De hoek waarin het fysiek bord gepositioneerd is ten opzichte van een vooropgestelde as.',
                                  owner=self)

    @property
    def foto(self) -> DtcDocumentWaarden:
        """Een foto van de opstelling zoals die te zien is op het openbaar domein."""
        return self._foto.get_waarde()

    @foto.setter
    def foto(self, value):
        self._foto.set_waarde(value, owner=self)

    @property
    def hoek(self) -> float:
        """De hoek waarin het fysiek bord gepositioneerd is ten opzichte van een vooropgestelde as."""
        return self._hoek.get_waarde()

    @hoek.setter
    def hoek(self, value):
        self._hoek.set_waarde(value, owner=self)
