# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.KlLEACPerformantieklasse import KlLEACPerformantieklasse
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefPerformantieklasse(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef die de performantie (bij impact) bepaalt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieklasse'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GetesteBeginconstructie', direction='o', deprecated='2.0.0')  # o = direction: outgoing

        self._performantieklasse = OTLAttribuut(field=KlLEACPerformantieklasse,
                                                naam='performantieklasse',
                                                label='performantieklasse',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieklasse.performantieklasse',
                                                usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                deprecated_version='2.0.0',
                                                definition='De aanduiding hoe (performantie) de beginconstructie is getest.',
                                                owner=self)

    @property
    def performantieklasse(self) -> str:
        """De aanduiding hoe (performantie) de beginconstructie is getest."""
        return self._performantieklasse.get_waarde()

    @performantieklasse.setter
    def performantieklasse(self, value):
        self._performantieklasse.set_waarde(value, owner=self)
