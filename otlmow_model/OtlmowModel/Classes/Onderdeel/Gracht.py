# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.WaterloopRelatie import WaterloopRelatie
from ...Datatypes.KlGrachtdoorsnede import KlGrachtdoorsnede
from ...Datatypes.KlGrachtFunctie import KlGrachtFunctie
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Gracht(WaterloopRelatie, LijnGeometrie):
    """Een kunstmatige aangelegde waterloop."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AanvullendeMiddellijn', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpenInfiltratievoorziening', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spaarbekken', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpenInfiltratievoorziening', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spaarbekken', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._doorsnede = OTLAttribuut(field=KlGrachtdoorsnede,
                                       naam='doorsnede',
                                       label='doorsnede',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht.doorsnede',
                                       definition='De doorsnede van de gracht.',
                                       owner=self)

        self._functie = OTLAttribuut(field=KlGrachtFunctie,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht.functie',
                                     definition='De functiebepaling van de gracht, als vesting, polder,...',
                                     owner=self)

        self._isBekleed = OTLAttribuut(field=BooleanField,
                                       naam='isBekleed',
                                       label='is bekleed',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Gracht.isBekleed',
                                       definition='Geeft aan of de oever en/of bodem van de gracht is voorzien van een kunstmatige bekleding (zoals beton, metselwerk, of kunststof), met het doel om de gracht te verstevigen, erosie te voorkomen, of het onderhoud te vergemakkelijken.',
                                       owner=self)

    @property
    def doorsnede(self) -> str:
        """De doorsnede van de gracht."""
        return self._doorsnede.get_waarde()

    @doorsnede.setter
    def doorsnede(self, value):
        self._doorsnede.set_waarde(value, owner=self)

    @property
    def functie(self) -> str:
        """De functiebepaling van de gracht, als vesting, polder,..."""
        return self._functie.get_waarde()

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)

    @property
    def isBekleed(self) -> bool:
        """Geeft aan of de oever en/of bodem van de gracht is voorzien van een kunstmatige bekleding (zoals beton, metselwerk, of kunststof), met het doel om de gracht te verstevigen, erosie te voorkomen, of het onderhoud te vergemakkelijken."""
        return self._isBekleed.get_waarde()

    @isBekleed.setter
    def isBekleed(self, value):
        self._isBekleed.set_waarde(value, owner=self)
