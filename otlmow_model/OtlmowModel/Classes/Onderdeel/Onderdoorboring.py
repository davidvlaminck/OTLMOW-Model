# coding=utf-8
from typing import List
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AbstracteAanvullendeGeometrie import AbstracteAanvullendeGeometrie
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInEuro import KwantWrdInEuro, KwantWrdInEuroWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderdoorboring(AbstracteAanvullendeGeometrie, LijnGeometrie, VlakGeometrie):
    """Gebruikt voor de registratie van kenmerken en de geometrie van een boring onder een weg of spoorweg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kabel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelkoker', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingskabel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermbuis', direction='i')  # i = direction: incoming

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
                                        kardinaliteit_max='*',
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
    def vergunning(self) -> List[DtcDocumentWaarden]:
        """Het document met de vergunning voor de onderdoorboring."""
        return self._vergunning.get_waarde()

    @vergunning.setter
    def vergunning(self, value):
        self._vergunning.set_waarde(value, owner=self)
