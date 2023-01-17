# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.IPNetwerkToegangObject import IPNetwerkToegangObject
from otlmow_model.Classes.Abstracten.RHZModule import RHZModule
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlDABRepeaterMerk import KlDABRepeaterMerk
from otlmow_model.Datatypes.KlDABRepeaterModelnaam import KlDABRepeaterModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DABRepeater(AIMNaamObject, IPNetwerkToegangObject, RHZModule):
    """DABRepeater is een radio-ontvanger en -zender, die het DAB-signaal ontvangt en weer doorgeeft om zo grotere afstanden te overbruggen en plaatsen te bereiken, waar de radiosignalen niet geraken, zoals in tunnels."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DABRepeater'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        IPNetwerkToegangObject.__init__(self)
        RHZModule.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort')

        self._merk = OTLAttribuut(field=KlDABRepeaterMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DABRepeater.merk',
                                  definition='Merknaam van de DAB repeater.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDABRepeaterModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DABRepeater.modelnaam',
                                       definition='Modelnaam van de DAB repeater.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DABRepeater.technischeFiche',
                                             definition='De technische fiche van de DAB repeater.',
                                             owner=self)

    @property
    def merk(self) -> str:
        """Merknaam van de DAB repeater."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Modelnaam van de DAB repeater."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de DAB repeater."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
