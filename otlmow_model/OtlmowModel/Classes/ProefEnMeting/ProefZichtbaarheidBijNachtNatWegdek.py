# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefZichtbaarheidBijNachtNatWegdek(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van het retroreflecterend vermogen van een markering bij nacht bij nat wegdek."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNachtNatWegdek'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', direction='o')  # o = direction: outgoing

        self._retrotreflectiecoëfficiënt = OTLAttribuut(field=FloatOrDecimalField,
                                                        naam='retrotreflectiecoëfficiënt',
                                                        label='retrotreflectiecoëfficiënt',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNachtNatWegdek.retrotreflectiecoëfficiënt',
                                                        usagenote='uitgedrukt in mcd. m-2.lux-1',
                                                        definition='De maat voor het retroreflecterend vermogen van een markering bij nacht bij nat wegdek.',
                                                        owner=self)

    @property
    def retrotreflectiecoëfficiënt(self) -> float:
        """De maat voor het retroreflecterend vermogen van een markering bij nacht bij nat wegdek."""
        return self._retrotreflectiecoëfficiënt.get_waarde()

    @retrotreflectiecoëfficiënt.setter
    def retrotreflectiecoëfficiënt(self, value):
        self._retrotreflectiecoëfficiënt.set_waarde(value, owner=self)
