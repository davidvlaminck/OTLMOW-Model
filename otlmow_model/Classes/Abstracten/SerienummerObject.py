# coding=utf-8
from otlmow_model.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from otlmow_model.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class SerienummerObject(ABC):
    """Abstracte klasse voor een serienummer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SerienummerObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SerienummerObject.serienummer',
                                         definition='Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.',
                                         owner=self)

    @property
    def serienummer(self) -> str:
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)
