# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.RHZModule import RHZModule
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlSignaalfilterMerk import KlSignaalfilterMerk
from ...Datatypes.KlSignaalfilterModelnaam import KlSignaalfilterModelnaam
from ...Datatypes.KlSignaalfilterType import KlSignaalfilterType
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Signaalfilter(RHZModule, SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een frequentiegestuurde module (in het bereik van 0 Hz tot 20 kHz) dat bepaalde frequentiebereiken kan versterken, doorlaten of verzwakken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalfilter'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', direction='u')  # u = unidirectional

        self._merk = OTLAttribuut(field=KlSignaalfilterMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalfilter.merk',
                                  definition='Het merk van van een signaalfilter.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlSignaalfilterModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalfilter.modelnaam',
                                       definition='De modelnaam van een signaalfilter.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalfilter.technischeFiche',
                                             definition='De technische fiche van een signaalfilter.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlSignaalfilterType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Signaalfilter.type',
                                  definition='Het type filter dat toegepast wordt op het signaal.',
                                  owner=self)

    @property
    def merk(self) -> str:
        """Het merk van van een signaalfilter."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van een signaalfilter."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van een signaalfilter."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self) -> str:
        """Het type filter dat toegepast wordt op het signaal."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
