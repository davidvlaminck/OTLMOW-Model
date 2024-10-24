# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.KwantWrdInCelsius import KwantWrdInCelsius, KwantWrdInCelsiusWaarden
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefTemperatuur(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Controle van de temperatuur van een asfaltmengsel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTemperatuur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging', direction='o')  # o = direction: outgoing

        self._temperatuur = OTLAttribuut(field=KwantWrdInCelsius,
                                         naam='temperatuur',
                                         label='temperatuur',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTemperatuur.temperatuur',
                                         definition='De temperatuur van de BV laag in graden Celsius.',
                                         owner=self)

    @property
    def temperatuur(self) -> KwantWrdInCelsiusWaarden:
        """De temperatuur van de BV laag in graden Celsius."""
        return self._temperatuur.get_waarde()

    @temperatuur.setter
    def temperatuur(self, value):
        self._temperatuur.set_waarde(value, owner=self)
