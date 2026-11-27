# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Bewegingsmechanisme import Bewegingsmechanisme
from ...Datatypes.KwantWrdInKilogram import (
    KwantWrdInKilogram,
    KwantWrdInKilogramWaarden,
)
from ...Datatypes.KwantWrdInKiloNewton import (
    KwantWrdInKiloNewton,
    KwantWrdInKiloNewtonWaarden,
)
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cilindermechanisme(Bewegingsmechanisme):
    """Abstracte om relaties en attributen te bundelen voor cilindermechanismen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Cilindermechanisme'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Grendelmechanisme', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CilinderStangkop', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderbodem', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderkop', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilindermantel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderstang', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._gewicht = OTLAttribuut(field=KwantWrdInKilogram,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Cilindermechanisme.gewicht',
                                     definition='Het gewicht, uitgedrukt in kilogram.',
                                     owner=self)

        self._maximaleKracht = OTLAttribuut(field=KwantWrdInKiloNewton,
                                            naam='maximaleKracht',
                                            label='maximale kracht',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Cilindermechanisme.maximaleKracht',
                                            definition='De kracht die overeenstemt met belastingsniveau 2 volgend uit de belastingscombinatie 2 van het SB270.',
                                            owner=self)

        self._slag = OTLAttribuut(field=KwantWrdInMillimeter,
                                  naam='slag',
                                  label='slag',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Cilindermechanisme.slag',
                                  definition='Afstand waarover de cilinder kan uitgeschoven worden.',
                                  owner=self)

    @property
    def gewicht(self) -> KwantWrdInKilogramWaarden:
        """Het gewicht, uitgedrukt in kilogram."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def maximaleKracht(self) -> KwantWrdInKiloNewtonWaarden:
        """De kracht die overeenstemt met belastingsniveau 2 volgend uit de belastingscombinatie 2 van het SB270."""
        return self._maximaleKracht.get_waarde()

    @maximaleKracht.setter
    def maximaleKracht(self, value):
        self._maximaleKracht.set_waarde(value, owner=self)

    @property
    def slag(self) -> KwantWrdInMillimeterWaarden:
        """Afstand waarover de cilinder kan uitgeschoven worden."""
        return self._slag.get_waarde()

    @slag.setter
    def slag(self, value):
        self._slag.set_waarde(value, owner=self)
