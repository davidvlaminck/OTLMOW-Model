# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KlElastischElementHardheid import KlElastischElementHardheid
from otlmow_model.Datatypes.KlElastischElementMateriaal import KlElastischElementMateriaal
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ElastischElement(SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Een elastisch of flexibel element is een onderdeel van een mechanische koppeling en zorgt voor het dempen van trillingen en schokken. Het wordt meestal tussen twee naven geplaatst."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ElastischElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Naaf')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Koppeling')

        self._hardheid = OTLAttribuut(field=KlElastischElementHardheid,
                                      naam='hardheid',
                                      label='hardheid',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ElastischElement.hardheid',
                                      definition='De hardheid van het elastisch element.',
                                      owner=self)

        self._materiaal = OTLAttribuut(field=KlElastischElementMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ElastischElement.materiaal',
                                       definition='Het materiaal waaruit het elastisch element vervaardigd is.',
                                       owner=self)

    @property
    def hardheid(self) -> str:
        """De hardheid van het elastisch element."""
        return self._hardheid.get_waarde()

    @hardheid.setter
    def hardheid(self, value):
        self._hardheid.set_waarde(value, owner=self)

    @property
    def materiaal(self) -> str:
        """Het materiaal waaruit het elastisch element vervaardigd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
