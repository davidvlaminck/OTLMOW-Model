# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.SerienummerObject import SerienummerObject
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInMeterTAW import (
    KwantWrdInMeterTAW,
    KwantWrdInMeterTAWWaarden,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Niveaumeting(SerienummerObject, AIMNaamObject, PuntGeometrie):
    """Abstracte om alle methodes van niveau- of peilmeting te groeperen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Niveaumeting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompkamer', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Silo', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tank', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pompstation', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Relais', 'u', None),  # u = unidirectional
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

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
