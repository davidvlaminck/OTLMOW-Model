# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.AbstracteAanvullendeGeometrie import AbstracteAanvullendeGeometrie
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.Datatypes.KwantWrdInEuro import KwantWrdInEuro, KwantWrdInEuroWaarden
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderdoorboring(AbstracteAanvullendeGeometrie, LijnGeometrie, VlakGeometrie):
    """Gebruikt voor de registratie van kenmerken en de geometrie van een boring onder een weg of spoorweg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._retributie = OTLAttribuut(field=KwantWrdInEuro,
                                        naam='retributie',
                                        label='retributie',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring.retributie',
                                        definition='Periodieke geldsom verschuldigd aan de eigenaar of beheerder van het terrein waaronder de onderboring ligt.',
                                        owner=self)

        self._vergunning = OTLAttribuut(field=DtcDocument,
                                        naam='vergunning',
                                        label='vergunning',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring.vergunning',
                                        definition='Het document met de vergunning voor de onderdoorboring.',
                                        owner=self)

    @property
    def retributie(self) -> KwantWrdInEuroWaarden:
        """Periodieke geldsom verschuldigd aan de eigenaar of beheerder van het terrein waaronder de onderboring ligt."""
        return self._retributie.get_waarde()

    @retributie.setter
    def retributie(self, value):
        self._retributie.set_waarde(value, owner=self)

    @property
    def vergunning(self) -> DtcDocumentWaarden:
        """Het document met de vergunning voor de onderdoorboring."""
        return self._vergunning.get_waarde()

    @vergunning.setter
    def vergunning(self, value):
        self._vergunning.set_waarde(value, owner=self)
