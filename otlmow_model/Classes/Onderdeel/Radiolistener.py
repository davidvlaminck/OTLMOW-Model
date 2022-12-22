# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.IPNetwerkToegangObject import IPNetwerkToegangObject
from otlmow_model.Classes.Abstracten.RHZModule import RHZModule
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlRadiolistenerMerk import KlRadiolistenerMerk
from otlmow_model.Datatypes.KlRadiolistenerModelnaam import KlRadiolistenerModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Radiolistener(IPNetwerkToegangObject, RHZModule, SerienummerObject, AIMNaamObject):
    """Een radiotoestel om de verschillende uitgezonden radiozenders (FM en DAB+) of boodschappen te beluisteren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radiolistener'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        IPNetwerkToegangObject.__init__(self)
        RHZModule.__init__(self)
        SerienummerObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')

        self._merk = OTLAttribuut(field=KlRadiolistenerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radiolistener.merk',
                                  definition='Merknaam van de radiolistener.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlRadiolistenerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radiolistener.modelnaam',
                                       definition='Modelnaam van de radiolistener.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Radiolistener.technischeFiche',
                                             definition='De technische fiche van de radiolistener.',
                                             owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van de radiolistener."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de radiolistener."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de radiolistener."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
