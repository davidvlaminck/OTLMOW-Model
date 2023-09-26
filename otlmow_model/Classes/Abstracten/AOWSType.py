# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from otlmow_model.BaseClasses.BooleanField import BooleanField
from otlmow_model.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AOWSType(ABC):
    """Abstracte om alle eigenschappen en relaties van AOWS type onder 1 noemer te houden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AOWSType'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._isGoedgekeurd = OTLAttribuut(field=BooleanField,
                                           naam='isGoedgekeurd',
                                           label='is goedgekeurd',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AOWSType.isGoedgekeurd',
                                           definition='Bepaling van de goedkeuring van AOWS.',
                                           owner=self)

        self._versieGoedgekeurd = OTLAttribuut(field=StringField,
                                               naam='versieGoedgekeurd',
                                               label='versie goedgekeurd',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AOWSType.versieGoedgekeurd',
                                               definition='De versie van het standaardbestek 250 waar de goedkeuring is bepaald.',
                                               owner=self)

    @property
    def isGoedgekeurd(self) -> bool:
        """Bepaling van de goedkeuring van AOWS."""
        return self._isGoedgekeurd.get_waarde()

    @isGoedgekeurd.setter
    def isGoedgekeurd(self, value):
        self._isGoedgekeurd.set_waarde(value, owner=self)

    @property
    def versieGoedgekeurd(self) -> str:
        """De versie van het standaardbestek 250 waar de goedkeuring is bepaald."""
        return self._versieGoedgekeurd.get_waarde()

    @versieGoedgekeurd.setter
    def versieGoedgekeurd(self, value):
        self._versieGoedgekeurd.set_waarde(value, owner=self)
