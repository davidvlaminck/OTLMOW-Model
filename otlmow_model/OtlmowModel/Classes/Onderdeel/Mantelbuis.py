# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Buis import Buis
from ...Classes.Abstracten.ContainerBuis import ContainerBuis
from ...Datatypes.KlRioleringsbuisMateriaal import KlRioleringsbuisMateriaal


# Generated with OTLClassCreator. To modify: extend, do not edit
class Mantelbuis(Buis, ContainerBuis):
    """Een ondergrondse buis bestemd voor de doorvoer van kabels en/of leidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.8.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i', deprecated='2.8.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omhult', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis', direction='i', deprecated='2.3.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', direction='i', deprecated='2.8.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', direction='i', deprecated='2.8.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', direction='i', deprecated='2.8.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', direction='i', deprecated='2.8.0')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', direction='i', deprecated='2.8.0')  # i = direction: incoming

        self._materiaal = OTLAttribuut(field=KlRioleringsbuisMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis.materiaal',
                                       usagenote='Klasse uit gebruik sinds versie 2.8.0 ',
                                       deprecated_version='2.8.0',
                                       definition='Bepaalt het materiaal van de mantelbuis.',
                                       owner=self)

    @property
    def materiaal(self) -> str:
        """Bepaalt het materiaal van de mantelbuis."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
