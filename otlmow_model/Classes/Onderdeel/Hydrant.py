# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.Brandvoorziening import Brandvoorziening
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.Datatypes.KlHydrantKoppeling import KlHydrantKoppeling
from otlmow_model.Datatypes.KwantWrdInInch import KwantWrdInInch, KwantWrdInInchWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hydrant(Brandvoorziening):
    """Aftappunt van de brandleiding bedoeld voor de brandweer. Ook brandkraan genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost')

        self._diameter = OTLAttribuut(field=KwantWrdInInch,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant.diameter',
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
    def diameter(self) -> KwantWrdInInchWaarden:
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
