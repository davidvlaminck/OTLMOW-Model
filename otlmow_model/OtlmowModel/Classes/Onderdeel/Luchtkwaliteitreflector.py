# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Luchtkwaliteittoestel import Luchtkwaliteittoestel


# Generated with OTLClassCreator. To modify: extend, do not edit
class Luchtkwaliteitreflector(Luchtkwaliteittoestel):
    """Onderdeel van de luchtkwaliteitsensor dat het signaal uitgestuurd door de LuchtkwaliteitZenderOntvanger reflecteert om de luchtkwaliteit tussen beiden onderdelen te kunnen meten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luchtkwaliteitreflector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Luchtkwaliteitsensor', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LKSensorDoorverbinddoos', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LKSensorDoorverbinddoos', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._isBeschermd = OTLAttribuut(field=BooleanField,
                                         naam='isBeschermd',
                                         label='is beschermd',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luchtkwaliteitreflector.isBeschermd',
                                         definition='Geeft aan of de sensor beschermd is tegen beschadiging, bv. door een aanrijding.',
                                         owner=self)

    @property
    def isBeschermd(self) -> bool:
        """Geeft aan of de sensor beschermd is tegen beschadiging, bv. door een aanrijding."""
        return self._isBeschermd.get_waarde()

    @isBeschermd.setter
    def isBeschermd(self, value):
        self._isBeschermd.set_waarde(value, owner=self)
