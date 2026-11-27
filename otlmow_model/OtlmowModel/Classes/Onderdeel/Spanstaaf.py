# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)
from ...Datatypes.KwantWrdInVierkanteMillimeter import (
    KwantWrdInVierkanteMillimeter,
    KwantWrdInVierkanteMillimeterWaarden,
)
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Spanstaaf(AIMNaamObject, LijnGeometrie):
    """Een staaf die gebruikt kan worden als externe naspanning."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanstaaf'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#ExterneNaspanning', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanstaaf.diameter',
                                      definition='De diameter van de spanstaaf, uitgedrukt in millimeter.',
                                      owner=self)

        self._sectieSpanstaaf = OTLAttribuut(field=KwantWrdInVierkanteMillimeter,
                                             naam='sectieSpanstaaf',
                                             label='sectie spanstaaf',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Spanstaaf.sectieSpanstaaf',
                                             definition='De staafdoorsnede, uitgedrukt in vierkante millimeter.',
                                             owner=self)

    @property
    def diameter(self) -> KwantWrdInMillimeterWaarden:
        """De diameter van de spanstaaf, uitgedrukt in millimeter."""
        return self._diameter.get_waarde()

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def sectieSpanstaaf(self) -> KwantWrdInVierkanteMillimeterWaarden:
        """De staafdoorsnede, uitgedrukt in vierkante millimeter."""
        return self._sectieSpanstaaf.get_waarde()

    @sectieSpanstaaf.setter
    def sectieSpanstaaf(self, value):
        self._sectieSpanstaaf.set_waarde(value, owner=self)
