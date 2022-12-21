# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from otlmow_model.Classes.Abstracten.ElektrischComponentennummerObject import ElektrischComponentennummerObject
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KlVeiligheidsrelaisMerk import KlVeiligheidsrelaisMerk
from otlmow_model.Datatypes.KlVeiligheidsrelaisModelnaam import KlVeiligheidsrelaisModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Veiligheidsrelais(ElektrischComponentennummerObject, SerienummerObject, AIMNaamObject):
    """Relais voor de bewaking van de noodstop binnen het noodstopcircuit. Voldoet omwille aan specifieke vereisten om te vermijden dat een storing tot een verlies van de veiligheidsfunctie kan leiden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veiligheidsrelais'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        ElektrischComponentennummerObject.__init__(self)
        SerienummerObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noodstopknop')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC')

        self._merk = OTLAttribuut(field=KlVeiligheidsrelaisMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veiligheidsrelais.merk',
                                  definition='Het merk van het veiligheidsrelais.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlVeiligheidsrelaisModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veiligheidsrelais.modelnaam',
                                       definition='De modelnaam van het veiligheidsrelais volgens de fabrikant.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veiligheidsrelais.technischeFiche',
                                             definition='De technische fiche van een veiligheidsrelais.',
                                             owner=self)

    @property
    def merk(self) -> str:
        """Het merk van het veiligheidsrelais."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """De modelnaam van het veiligheidsrelais volgens de fabrikant."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van een veiligheidsrelais."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
