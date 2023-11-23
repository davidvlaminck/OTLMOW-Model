# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Buis import Buis
from ...Datatypes.KlPersleidingMateriaal import KlPersleidingMateriaal
from ...Datatypes.KlSDRKlasse import KlSDRKlasse
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Persleiding(Buis, LijnGeometrie):
    """Ondergronds kanaal of pijp voor afvoer van een vloeistof of gas onder druk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurdoorgangsstuk')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stuurklep')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank')

        self._materiaal = OTLAttribuut(field=KlPersleidingMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding.materiaal',
                                       definition='Bepaalt het materiaal van de persleiding.',
                                       owner=self)

        self._sdrKlasse = OTLAttribuut(field=KlSDRKlasse,
                                       naam='sdrKlasse',
                                       label='SDR klasse',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Persleiding.sdrKlasse',
                                       definition='De verhouding tussen de wanddikte en de diameter van de persleiding.',
                                       owner=self)

    @property
    def materiaal(self) -> str:
        """Bepaalt het materiaal van de persleiding."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def sdrKlasse(self) -> str:
        """De verhouding tussen de wanddikte en de diameter van de persleiding."""
        return self._sdrKlasse.get_waarde()

    @sdrKlasse.setter
    def sdrKlasse(self, value):
        self._sdrKlasse.set_waarde(value, owner=self)
