# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class ElektrischComponentennummerObject(ABC):
    """Abstracte voor Objecttypes waarvoor het componentnummer op het lokale elektrische schema moet bijgehouden worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ElektrischComponentennummerObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._componentnummer = OTLAttribuut(field=StringField,
                                             naam='componentnummer',
                                             label='componentnummer',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ElektrischComponentennummerObject.componentnummer',
                                             definition='Het componentnummer van het elektrische toestel, zoals weergegeven op het schema van het lokale laagspanningsbord. Wordt ook wel onderdeelcode (ODC) genoemd.',
                                             owner=self)

    @property
    def componentnummer(self) -> str:
        """Het componentnummer van het elektrische toestel, zoals weergegeven op het schema van het lokale laagspanningsbord. Wordt ook wel onderdeelcode (ODC) genoemd."""
        return self._componentnummer.get_waarde()

    @componentnummer.setter
    def componentnummer(self, value):
        self._componentnummer.set_waarde(value, owner=self)
