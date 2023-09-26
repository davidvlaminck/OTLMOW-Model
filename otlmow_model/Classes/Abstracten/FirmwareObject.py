# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from otlmow_model.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class FirmwareObject(ABC):
    """Abstracte voor de firmware van het object."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#FirmwareObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._firmwareversie = OTLAttribuut(field=StringField,
                                            naam='firmwareversie',
                                            label='firmwareversie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#FirmwareObject.firmwareversie',
                                            definition='Versie van de firmware.',
                                            owner=self)

    @property
    def firmwareversie(self) -> str:
        """Versie van de firmware."""
        return self._firmwareversie.get_waarde()

    @firmwareversie.setter
    def firmwareversie(self, value):
        self._firmwareversie.set_waarde(value, owner=self)
