# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefStaalvezelgehalte(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van de hoeveelheid staalvezels in de cementbetonverharding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStaalvezelgehalte'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding', direction='o')  # o = direction: outgoing

        self._staalvezelgehalte = OTLAttribuut(field=DtcDocument,
                                               naam='staalvezelgehalte',
                                               label='staalvezelgehalte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStaalvezelgehalte.staalvezelgehalte',
                                               definition='Het resultaat van de test van het gemeten staalvezelgehalte in de BV laag.',
                                               owner=self)

    @property
    def staalvezelgehalte(self) -> DtcDocumentWaarden:
        """Het resultaat van de test van het gemeten staalvezelgehalte in de BV laag."""
        return self._staalvezelgehalte.get_waarde()

    @staalvezelgehalte.setter
    def staalvezelgehalte(self, value):
        self._staalvezelgehalte.set_waarde(value, owner=self)
