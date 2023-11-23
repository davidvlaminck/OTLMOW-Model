# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from otlmow_model.OtlmowModel.BaseClasses.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Waterremmend(ABC):
    """Abstracte voor onderdelen die waterremmend kunnen zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waterremmend'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._heeftWaterremmendeFunctie = OTLAttribuut(field=BooleanField,
                                                       naam='heeftWaterremmendeFunctie',
                                                       label='heeft waterremmende functie',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waterremmend.heeftWaterremmendeFunctie',
                                                       definition='Geeft aan of de installatie een waterremmende functie heeft of niet.',
                                                       owner=self)

    @property
    def heeftWaterremmendeFunctie(self) -> bool:
        """Geeft aan of de installatie een waterremmende functie heeft of niet."""
        return self._heeftWaterremmendeFunctie.get_waarde()

    @heeftWaterremmendeFunctie.setter
    def heeftWaterremmendeFunctie(self, value):
        self._heeftWaterremmendeFunctie.set_waarde(value, owner=self)
