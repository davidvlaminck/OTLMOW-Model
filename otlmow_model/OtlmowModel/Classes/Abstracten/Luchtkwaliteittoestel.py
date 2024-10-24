# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlLuchtkwaliteitOpstellingMerk import KlLuchtkwaliteitOpstellingMerk
from ...Datatypes.KlLuchtkwaliteitOpstellingModelnaam import KlLuchtkwaliteitOpstellingModelnaam
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Luchtkwaliteittoestel(AIMNaamObject, PuntGeometrie):
    """Abstracte voor attributen van onderdelen van de luchtkwaliteitsensor installatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BekledingComponent', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorzetconstructie', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlLuchtkwaliteitOpstellingMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel.merk',
                                  definition='Het merk van een onderdeel uit een luchtkwaliteitsinstallatie.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlLuchtkwaliteitOpstellingModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Luchtkwaliteittoestel.modelnaam',
                                       definition='De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """Het merk van een onderdeel uit een luchtkwaliteitsinstallatie."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
