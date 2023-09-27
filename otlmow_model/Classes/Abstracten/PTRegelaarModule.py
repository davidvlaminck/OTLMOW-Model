# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlPTRegelaarModuleMerk import KlPTRegelaarModuleMerk
from otlmow_model.Datatypes.KlPTRegelaarModuleModelnaam import KlPTRegelaarModuleModelnaam
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTRegelaarModule(AIMNaamObject, PuntGeometrie):
    """Abstracte voor de verschillende modules waaruit het personentransportbeïnvloedingssysteem van de verkeersregelaar opgebouwd is. Hierdoor zal het personentransport een snellere doorstroming aan een verkeerslichtengeregeld kruispunt genieten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTRegelaarModule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar')

        self._merk = OTLAttribuut(field=KlPTRegelaarModuleMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTRegelaarModule.merk',
                                  definition='Het merk van de PT regelaar module.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlPTRegelaarModuleModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PTRegelaarModule.modelnaam',
                                       definition='De modelnaam/product range van de PT regelaar module.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van de PT regelaar module."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam/product range van de PT regelaar module."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
