# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.Proef import Proef
from otlmow_model.Datatypes.KlLEACPerformantieniveau import KlLEACPerformantieniveau
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefPerformantieniveau(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Bepaling van het performantieniveau."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieniveau'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger', deprecated='2.0.0')

        self._performantieniveau = OTLAttribuut(field=KlLEACPerformantieniveau,
                                                naam='performantieniveau',
                                                label='performantieniveau',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieniveau.performantieniveau',
                                                usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                                deprecated_version='2.0.0',
                                                definition='Het niveau waarop de obstakelbeveiliger is getest.',
                                                owner=self)

    @property
    def performantieniveau(self) -> str:
        """Het niveau waarop de obstakelbeveiliger is getest."""
        return self._performantieniveau.get_waarde()

    @performantieniveau.setter
    def performantieniveau(self, value):
        self._performantieniveau.set_waarde(value, owner=self)
