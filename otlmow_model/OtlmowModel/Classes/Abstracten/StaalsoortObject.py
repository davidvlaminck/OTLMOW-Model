# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from ...Datatypes.KlStaalsoortMetEquivalenten import KlStaalsoortMetEquivalenten


# Generated with OTLClassCreator. To modify: extend, do not edit
class StaalsoortObject(ABC):
    """Abstracte met staalsoorten"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StaalsoortObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._materiaal = OTLAttribuut(field=KlStaalsoortMetEquivalenten,
                                       naam='materiaal',
                                       label='staalsoorten',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StaalsoortObject.materiaal',
                                       definition='Lijst van staalsoorten (constructiestaal, gietstaal, veredelstaal, smeedstaan en roestvaststaal)',
                                       owner=self)

    @property
    def materiaal(self) -> str:
        """Lijst van staalsoorten (constructiestaal, gietstaal, veredelstaal, smeedstaan en roestvaststaal)"""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)
