# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDoorlatendheid(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """De controle van de doorlatendheid van het oppervlak met behulp van de dubbele ringmethode."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDoorlatendheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating', direction='o')  # o = direction: outgoing

        self._doorlatendheid = OTLAttribuut(field=DtcDocument,
                                            naam='doorlatendheid',
                                            label='doorlatendheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDoorlatendheid.doorlatendheid',
                                            definition='Proefresultaten van de waterdoorlatendheid.',
                                            owner=self)

    @property
    def doorlatendheid(self) -> DtcDocumentWaarden:
        """Proefresultaten van de waterdoorlatendheid."""
        return self._doorlatendheid.get_waarde()

    @doorlatendheid.setter
    def doorlatendheid(self, value):
        self._doorlatendheid.set_waarde(value, owner=self)
