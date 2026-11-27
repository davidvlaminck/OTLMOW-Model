# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LinkendElement import LinkendElement
from ...Datatypes.KwantWrdInKubiekeMeterPerSeconde import (
    KwantWrdInKubiekeMeterPerSeconde,
    KwantWrdInKubiekeMeterPerSecondeWaarden,
)
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)


# Generated with OTLClassCreator. To modify: extend, do not edit
class PompSchroefEnWaaier(LinkendElement):
    """Abstracte die alle relaties van pomp schroeven en waaiers verzamelt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PompSchroefEnWaaier'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aandrijfas', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pomphuis', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#PompGroep', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Brandvoorziening', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkendElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurdoorgangsstuk', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PutRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#WaterloopRelatie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurdoorgangsstuk', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PompSchroefEnWaaier.diameter',
                                      definition='Diameter van de pompschroef of pompwaaier, inclusief de eigenlijke spiraal. Dit is dus de diameter die een omhullende cilinder nodig zou hebben.',
                                      owner=self)

        self._maximaalDebietPomp = OTLAttribuut(field=KwantWrdInKubiekeMeterPerSeconde,
                                                naam='maximaalDebietPomp',
                                                label='maximaal debiet pomp',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PompSchroefEnWaaier.maximaalDebietPomp',
                                                definition='Het debiet dat de pomp kan verplaatsen wanneer ze op volle capaciteit werkt volgens de specificaties van de fabrikant.',
                                                owner=self)

        self._maximaalDebietTurbine = OTLAttribuut(field=KwantWrdInKubiekeMeterPerSeconde,
                                                   naam='maximaalDebietTurbine',
                                                   label='maximaal debiet turbine',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#PompSchroefEnWaaier.maximaalDebietTurbine',
                                                   definition='Het debiet dat de pomp kan verplaatsen wanneer ze op volle capaciteit werkt volgens de specificaties van de fabrikant., wanneer deze in turbine stand gebruikt wordt.',
                                                   owner=self)

    @property
    def diameter(self) -> KwantWrdInMillimeterWaarden:
        """Diameter van de pompschroef of pompwaaier, inclusief de eigenlijke spiraal. Dit is dus de diameter die een omhullende cilinder nodig zou hebben."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def maximaalDebietPomp(self) -> KwantWrdInKubiekeMeterPerSecondeWaarden:
        """Het debiet dat de pomp kan verplaatsen wanneer ze op volle capaciteit werkt volgens de specificaties van de fabrikant."""
        return self._maximaalDebietPomp.get_waarde()

    @maximaalDebietPomp.setter
    def maximaalDebietPomp(self, value):
        self._maximaalDebietPomp.set_waarde(value, owner=self)

    @property
    def maximaalDebietTurbine(self) -> KwantWrdInKubiekeMeterPerSecondeWaarden:
        """Het debiet dat de pomp kan verplaatsen wanneer ze op volle capaciteit werkt volgens de specificaties van de fabrikant., wanneer deze in turbine stand gebruikt wordt."""
        return self._maximaalDebietTurbine.get_waarde()

    @maximaalDebietTurbine.setter
    def maximaalDebietTurbine(self, value):
        self._maximaalDebietTurbine.set_waarde(value, owner=self)
