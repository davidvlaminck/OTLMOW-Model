# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.KlLEACSchokindex import KlLEACSchokindex
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefSchokindex(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef voor de bepaling van de schokindex parameter."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindex'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie', 'o', '2.0.0'),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GetesteBeginconstructie', 'o', '2.0.0'),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger', 'o', '2.0.0'),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overgangsconstructie', 'o', '2.0.0'),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._schokindex = OTLAttribuut(field=KlLEACSchokindex,
                                        naam='schokindex',
                                        label='schokindex',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindex.schokindex',
                                        usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                        deprecated_version='2.0.0',
                                        definition='De parameter die weergeeft hoe groot de kans op ernstige letsels is van de inzittenden bij een aanrijding.',
                                        owner=self)

    @property
    def schokindex(self) -> str:
        """De parameter die weergeeft hoe groot de kans op ernstige letsels is van de inzittenden bij een aanrijding."""
        return self._schokindex.get_waarde()

    @schokindex.setter
    def schokindex(self, value):
        self._schokindex.set_waarde(value, owner=self)
