# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Brandvoorziening import Brandvoorziening
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlHydrantKoppeling import KlHydrantKoppeling
from ...Datatypes.KwantWrdInInch import KwantWrdInInch, KwantWrdInInchWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hydrant(Brandvoorziening, NaampadObject):
    """Aftappunt van de brandleiding bedoeld voor de brandweer. Ook brandkraan genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._diameter = OTLAttribuut(field=KwantWrdInInch,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant.diameter',
                                      kardinaliteit_max='*',
                                      definition='Diameter van het aftappunt.',
                                      owner=self)

        self._heeftEigenAfsluitkraan = OTLAttribuut(field=BooleanField,
                                                    naam='heeftEigenAfsluitkraan',
                                                    label='heeft eigen afsluitkraan',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant.heeftEigenAfsluitkraan',
                                                    definition='Geeft aan of de hydrant ter plaatse kan afgesloten/opengezet kan worden.',
                                                    owner=self)

        self._heeftIsolatie = OTLAttribuut(field=BooleanField,
                                           naam='heeftIsolatie',
                                           label='heeft isolatie',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant.heeftIsolatie',
                                           definition='Geeft aan of de hydrant voorzien is van eigen isolatie.',
                                           owner=self)

        self._koppeling = OTLAttribuut(field=KlHydrantKoppeling,
                                       naam='koppeling',
                                       label='koppeling',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant.koppeling',
                                       definition='Aard van de koppeling voor aansluiting van een aftapping.',
                                       owner=self)

    @property
    def diameter(self) -> list[KwantWrdInInchWaarden]:
        """Diameter van het aftappunt."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def heeftEigenAfsluitkraan(self) -> bool:
        """Geeft aan of de hydrant ter plaatse kan afgesloten/opengezet kan worden."""
        return self._heeftEigenAfsluitkraan.get_waarde()

    @heeftEigenAfsluitkraan.setter
    def heeftEigenAfsluitkraan(self, value):
        self._heeftEigenAfsluitkraan.set_waarde(value, owner=self)

    @property
    def heeftIsolatie(self) -> bool:
        """Geeft aan of de hydrant voorzien is van eigen isolatie."""
        return self._heeftIsolatie.get_waarde()

    @heeftIsolatie.setter
    def heeftIsolatie(self, value):
        self._heeftIsolatie.set_waarde(value, owner=self)

    @property
    def koppeling(self) -> str:
        """Aard van de koppeling voor aansluiting van een aftapping."""
        return self._koppeling.get_waarde()

    @koppeling.setter
    def koppeling(self, value):
        self._koppeling.set_waarde(value, owner=self)
