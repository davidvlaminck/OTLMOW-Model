# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Geleidingsmechanisme import Geleidingsmechanisme
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInKiloNewton import (
    KwantWrdInKiloNewton,
    KwantWrdInKiloNewtonWaarden,
)


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bufferinstallatie(Geleidingsmechanisme, AIMNaamObject):
    """Een verzameling van elementen die gebruikt worden om krachten of schokken op te vangen en te dempen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bufferinstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bovenrolwagen', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelbewegingsmechanisme', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Onderrolwagen', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buffercilinder', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draagstoel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Drukvat', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Houdriem', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stootblok', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veerhuis', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verenpakket', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._karakteristiekeToelaatbareBelasting = OTLAttribuut(field=KwantWrdInKiloNewton,
                                                                 naam='karakteristiekeToelaatbareBelasting',
                                                                 label='karakteristieke toelaatbare belasting',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bufferinstallatie.karakteristiekeToelaatbareBelasting',
                                                                 definition='De karakteristieke maximale toelaatbare belasting van de buffer, uitgedrukt in kilonewton.',
                                                                 owner=self)

    @property
    def karakteristiekeToelaatbareBelasting(self) -> KwantWrdInKiloNewtonWaarden:
        """De karakteristieke maximale toelaatbare belasting van de buffer, uitgedrukt in kilonewton."""
        return self._karakteristiekeToelaatbareBelasting.get_waarde()

    @karakteristiekeToelaatbareBelasting.setter
    def karakteristiekeToelaatbareBelasting(self, value):
        self._karakteristiekeToelaatbareBelasting.set_waarde(value, owner=self)
