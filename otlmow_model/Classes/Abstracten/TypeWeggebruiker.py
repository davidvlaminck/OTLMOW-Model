# coding=utf-8
from otlmow_model.BaseClasses.OTLObject import OTLAttribuut
from abc import abstractmethod, ABC
from otlmow_model.Datatypes.KlVriTypeweggebruiker import KlVriTypeweggebruiker


# Generated with OTLClassCreator. To modify: extend, do not edit
class TypeWeggebruiker(ABC):
    """Abstracte klasse die het type weggebruiker met een attribuut (volgens keuzelijst) aangeeft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TypeWeggebruiker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._typeWeggebruiker = OTLAttribuut(field=KlVriTypeweggebruiker,
                                              naam='typeWeggebruiker',
                                              label='type weggebruiker',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#TypeWeggebruiker.typeWeggebruiker',
                                              definition='het type weggebruiker.',
                                              owner=self)

    @property
    def typeWeggebruiker(self) -> str:
        """het type weggebruiker."""
        return self._typeWeggebruiker.get_waarde()

    @typeWeggebruiker.setter
    def typeWeggebruiker(self, value):
        self._typeWeggebruiker.set_waarde(value, owner=self)
