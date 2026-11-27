# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcAfmetingBxlInM import DtcAfmetingBxlInM, DtcAfmetingBxlInMWaarden
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wilddetectiezone(AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """De wilddetectiezone van een wilddetectiesysteem betreft de nabije zone rond de detectiesystemen (zoals een bewegingssensor). Deze zone vereist extra onderhoud, om valse detecties te voorkomen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wilddetectiezone'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bewegingssensor', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ecoraster', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._afmeting = OTLAttribuut(field=DtcAfmetingBxlInM,
                                      naam='afmeting',
                                      label='afmetingen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wilddetectiezone.afmeting',
                                      definition='De afmetingen van de wilddetectiezone.',
                                      owner=self)

    @property
    def afmeting(self) -> DtcAfmetingBxlInMWaarden:
        """De afmetingen van de wilddetectiezone."""
        return self._afmeting.get_waarde()

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)
