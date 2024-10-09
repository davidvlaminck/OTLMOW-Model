# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefZichtbaarheidBijDagOfWV(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de luminantiecoëfficiënt bij diffuse verlichting van een gemarkeerd oppervlak (Qd) bij daglicht of onder openbare verlichting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijDagOfWV'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', direction='o')  # o = direction: outgoing

        self._luminantiecoëfficiënt = OTLAttribuut(field=FloatOrDecimalField,
                                                   naam='luminantiecoëfficiënt',
                                                   label='luminantiecoëfficient',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijDagOfWV.luminantiecoëfficiënt',
                                                   usagenote='uitgedrukt in mcd. m-2.lux-1',
                                                   definition='De verhouding van de luminantie van het oppervlak in een gegeven richting en de verlichtingssterkte op het oppervlak.',
                                                   owner=self)

    @property
    def luminantiecoëfficiënt(self) -> float:
        """De verhouding van de luminantie van het oppervlak in een gegeven richting en de verlichtingssterkte op het oppervlak."""
        return self._luminantiecoëfficiënt.get_waarde()

    @luminantiecoëfficiënt.setter
    def luminantiecoëfficiënt(self, value):
        self._luminantiecoëfficiënt.set_waarde(value, owner=self)
