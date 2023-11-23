# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from ...Datatypes.KlAardingskabelSectie import KlAardingskabelSectie


# Generated with OTLClassCreator. To modify: extend, do not edit
class KabelAardingSamenstelling(ABC):
    """Abstracte voor eigenschappen van verschillende types kabel gebruikt voor aardingen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelAardingSamenstelling'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._sectie = OTLAttribuut(field=KlAardingskabelSectie,
                                    naam='sectie',
                                    label='sectie',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelAardingSamenstelling.sectie',
                                    definition='Geeft de dikte van een kabel of pen voor aarding weer als oppervlakte van een doorsnede, uitgedrukt in mm².',
                                    owner=self)

    @property
    def sectie(self) -> str:
        """Geeft de dikte van een kabel of pen voor aarding weer als oppervlakte van een doorsnede, uitgedrukt in mm²."""
        return self._sectie.get_waarde()

    @sectie.setter
    def sectie(self, value):
        self._sectie.set_waarde(value, owner=self)
