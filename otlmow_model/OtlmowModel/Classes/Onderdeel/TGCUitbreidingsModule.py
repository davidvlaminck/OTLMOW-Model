# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTGCUitbreidingsModuleMerk import KlTGCUitbreidingsModuleMerk
from ...Datatypes.KlTGCUitbreidingsModuleModelnaam import KlTGCUitbreidingsModuleModelnaam
from ...Datatypes.KlTGCUitbreidingsModuleType import KlTGCUitbreidingsModuleType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class TGCUitbreidingsModule(AIMNaamObject, PuntGeometrie):
    """Toestel dat kan gebruikt worden als een uitbreiding van de toegangscontroller."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TGCUitbreidingsModule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Binnenverlichtingstoestel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Magneetgrendel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slot', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontroller', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlTGCUitbreidingsModuleMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TGCUitbreidingsModule.merk',
                                  definition='De merknaam van de uitbreidingsmodule van een toegangscontroller.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlTGCUitbreidingsModuleModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TGCUitbreidingsModule.modelnaam',
                                       definition='De modelnaam van de uitbreidingsmodule van een toegangscontroller.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlTGCUitbreidingsModuleType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TGCUitbreidingsModule.type',
                                  definition='Het type uitbreidingsmodule van een toegangscontroller. Mogelijke types zijn deurmodules, IO modules of IP modules.',
                                  owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van de uitbreidingsmodule van een toegangscontroller."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van de uitbreidingsmodule van een toegangscontroller."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type uitbreidingsmodule van een toegangscontroller. Mogelijke types zijn deurmodules, IO modules of IP modules."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
