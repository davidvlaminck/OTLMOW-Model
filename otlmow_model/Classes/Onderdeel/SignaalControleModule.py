# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.RHZModule import RHZModule
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlSignaalControleModuleMerk import KlSignaalControleModuleMerk
from otlmow_model.Datatypes.KlSignaalControleModuleModelnaam import KlSignaalControleModuleModelnaam
from otlmow_model.Datatypes.KlSignaalControleModuleType import KlSignaalControleModuleType
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SignaalControleModule(AIMNaamObject, RHZModule, SerienummerObject, PuntGeometrie):
    """Een controlemodule dat nagaat of een specifiek (meestal DC-)signaal nog aanwezig is of dat de signaal/ruis-verhouding niet te laag is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalControleModule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        RHZModule.__init__(self)
        SerienummerObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=KlSignaalControleModuleMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalControleModule.merk',
                                  definition='Merknaam van de signaal controle module.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSignaalControleModuleModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalControleModule.modelnaam',
                                       definition='Modelnaam van de signaal controle module.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalControleModule.technischeFiche',
                                             definition='De technische fiche van de signaal controle module.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlSignaalControleModuleType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SignaalControleModule.type',
                                  definition='Het type van detectie dat uitgevoerd wordt door de signaal controle module.',
                                  owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van de signaal controle module."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de signaal controle module."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de signaal controle module."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type van detectie dat uitgevoerd wordt door de signaal controle module."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
