# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalBusEnRing import KlMateriaalBusEnRing
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class RingMechanisch(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een cirkelvormig, meestal metalen object, dat wordt gebruikt als verbindings-, afdichtings- of ondersteuningselement in mechanische constructies. De hoogte is kleiner dan of gelijk aan de wanddikte."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RingMechanisch'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rolgeleiding', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Scharnierpunt', direction='o')  # o = direction: outgoing

        self._materiaalRing = OTLAttribuut(field=KlMateriaalBusEnRing,
                                           naam='materiaalRing',
                                           label='materiaal ring',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RingMechanisch.materiaalRing',
                                           definition='Het materiaal waaruit de ring is vervaardigd.',
                                           owner=self)

    @property
    def materiaalRing(self) -> str:
        """Het materiaal waaruit de ring is vervaardigd."""
        return self._materiaalRing.get_waarde()

    @materiaalRing.setter
    def materiaalRing(self, value):
        self._materiaalRing.set_waarde(value, owner=self)
