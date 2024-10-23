# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Behuizing import Behuizing
from ...Datatypes.KlAlgMateriaal import KlAlgMateriaal
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class TechnischePut(Behuizing, PuntGeometrie, VlakGeometrie):
    """Ondergrondse toezichtsput (manhole). Deze kan telecom installaties (glasvezel,koper) of elektriciteitskabels bevatten. Kan uit verschillende materialen bestaan: polycarbonaat,beton,gemetst,of staal."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TechnischePut'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Toegangselement', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw', direction='u', deprecated='2.1.0')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw', direction='u')  # u = unidirectional

        self._materiaal = OTLAttribuut(field=KlAlgMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TechnischePut.materiaal',
                                       definition='Het materiaal waaruit de technische put opgebouwd is.',
                                       owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit de technische put opgebouwd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
