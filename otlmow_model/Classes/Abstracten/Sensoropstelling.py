# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from otlmow_model.Classes.Abstracten.Sensor import Sensor
from otlmow_model.Datatypes.KlSensorOpstelwijze import KlSensorOpstelwijze
from otlmow_model.Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sensoropstelling(Sensor):
    """Abstracte voor de gemeenschappelijke eigenschappen en relaties van de sensoren op een draagconstructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensoropstelling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie')

        self._opstelhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opstelhoogte',
                                          label='opstelhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensoropstelling.opstelhoogte',
                                          definition='De hoogte van de bevestiging van de sensor aan de draaconstructie.',
                                          owner=self)

        self._opstelwijze = OTLAttribuut(field=KlSensorOpstelwijze,
                                         naam='opstelwijze',
                                         label='opstelwijze',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Sensoropstelling.opstelwijze',
                                         definition='De manier waarop de meteosensor is opgesteld, bv. via dwarsligger,...',
                                         owner=self)

    @property
    def opstelhoogte(self) -> KwantWrdInMeterWaarden:
        """De hoogte van de bevestiging van de sensor aan de draaconstructie."""
        return self._opstelhoogte.get_waarde()

    @opstelhoogte.setter
    def opstelhoogte(self, value):
        self._opstelhoogte.set_waarde(value, owner=self)

    @property
    def opstelwijze(self) -> str:
        """De manier waarop de meteosensor is opgesteld, bv. via dwarsligger,..."""
        return self._opstelwijze.get_waarde()

    @opstelwijze.setter
    def opstelwijze(self, value):
        self._opstelwijze.set_waarde(value, owner=self)
