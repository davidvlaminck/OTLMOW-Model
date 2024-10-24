# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWeerstandAfschilfering(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Controle van de vorst-dooiweerstand volgens CEN/TS 12390-9."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWeerstandAfschilfering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding', direction='o')  # o = direction: outgoing

        self._weerstandAfschilfering = OTLAttribuut(field=DtcDocument,
                                                    naam='weerstandAfschilfering',
                                                    label='weerstand afschilfering',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWeerstandAfschilfering.weerstandAfschilfering',
                                                    definition='Proef om de weerstand/afschilfering van de laag te bepalen.',
                                                    owner=self)

    @property
    def weerstandAfschilfering(self) -> DtcDocumentWaarden:
        """Proef om de weerstand/afschilfering van de laag te bepalen."""
        return self._weerstandAfschilfering.get_waarde()

    @weerstandAfschilfering.setter
    def weerstandAfschilfering(self, value):
        self._weerstandAfschilfering.set_waarde(value, owner=self)
