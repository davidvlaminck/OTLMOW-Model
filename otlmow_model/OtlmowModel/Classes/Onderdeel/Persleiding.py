# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Buis import Buis
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlPersleidingMateriaal import KlPersleidingMateriaal
from ...Datatypes.KlSDRKlasse import KlSDRKlasse
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Persleiding(Buis, NaampadObject, LijnGeometrie):
    """Ondergronds kanaal of pijp voor afvoer van een vloeistof of gas onder druk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Debietmeter', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', '2.8.0'),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurdoorgangsstuk', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KWSAfscheider', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurdoorgangsstuk', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stuurklep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stuurklep', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._materiaal = OTLAttribuut(field=KlPersleidingMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding.materiaal',
                                       definition='Bepaalt het materiaal van de persleiding.',
                                       owner=self)

        self._sdrKlasse = OTLAttribuut(field=KlSDRKlasse,
                                       naam='sdrKlasse',
                                       label='SDR klasse',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding.sdrKlasse',
                                       definition='De verhouding tussen de wanddikte en de diameter van de persleiding.',
                                       owner=self)

    @property
    def materiaal(self) -> str:
        """Bepaalt het materiaal van de persleiding."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def sdrKlasse(self) -> str:
        """De verhouding tussen de wanddikte en de diameter van de persleiding."""
        return self._sdrKlasse.get_waarde()

    @sdrKlasse.setter
    def sdrKlasse(self, value):
        self._sdrKlasse.set_waarde(value, owner=self)
