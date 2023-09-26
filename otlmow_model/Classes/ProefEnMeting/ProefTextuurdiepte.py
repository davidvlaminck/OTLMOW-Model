# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefTextuurdiepte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de uitwasdiepte van de verharding na een oppervlaktebehandeling volgens NBN EN ISO 13473-1."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTextuurdiepte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding')

        self._textuurdiepte = OTLAttribuut(field=DtcDocument,
                                           naam='textuurdiepte',
                                           label='textuurdiepte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTextuurdiepte.textuurdiepte',
                                           definition='Proefresultaten van de textuurdiepte van de toplaag.',
                                           owner=self)

    @property
    def textuurdiepte(self) -> DtcDocumentWaarden:
        """Proefresultaten van de textuurdiepte van de toplaag."""
        return self._textuurdiepte.get_waarde()

    @textuurdiepte.setter
    def textuurdiepte(self, value):
        self._textuurdiepte.set_waarde(value, owner=self)
