# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefLuminantie(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bij gebrek aan Qd-meting kan de luminantiefactor ß van wegmarkeringen gebruikt worden om het contrast met het wegdek en bijgevolg de dagzichtbaarheid te bepalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuminantie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', direction='o')  # o = direction: outgoing

        self._luminantiefactor = OTLAttribuut(field=FloatOrDecimalField,
                                              naam='luminantiefactor',
                                              label='luminantiefactor',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuminantie.luminantiefactor',
                                              definition='Waarde om het contrast met het wegdek en bijgevolg de dagzichtbaarheid te bepalen.',
                                              owner=self)

    @property
    def luminantiefactor(self) -> float:
        """Waarde om het contrast met het wegdek en bijgevolg de dagzichtbaarheid te bepalen."""
        return self._luminantiefactor.get_waarde()

    @luminantiefactor.setter
    def luminantiefactor(self, value):
        self._luminantiefactor.set_waarde(value, owner=self)
