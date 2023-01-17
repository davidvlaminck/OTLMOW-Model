# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.SerienummerObject import SerienummerObject
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW, KwantWrdInMeterTAWWaarden
from otlmow_model.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Niveaumeting(AIMNaamObject, SerienummerObject, PuntGeometrie):
    """Abstracte om alle methodes van niveau- of peilmeting te groeperen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Niveaumeting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        SerienummerObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC')

        self._meetbereik = OTLAttribuut(field=KwantWrdInMeterTAW,
                                        naam='meetbereik',
                                        label='meetbereik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Niveaumeting.meetbereik',
                                        definition='Het meetbereik van de niveaumeting, uitgedrukt in meter TAW.',
                                        owner=self)

    @property
    def meetbereik(self) -> KwantWrdInMeterTAWWaarden:
        """Het meetbereik van de niveaumeting, uitgedrukt in meter TAW."""
        return self._meetbereik.get_waarde()

    @meetbereik.setter
    def meetbereik(self, value):
        self._meetbereik.set_waarde(value, owner=self)
