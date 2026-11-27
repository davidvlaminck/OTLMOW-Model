# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Proef import Proef
from ...Datatypes.KlLEACSchokindexMVP import KlLEACSchokindexMVP
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefSchokindexMVP(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef voor de bepaling van de schokindex parameter van de motorvangplank."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindexMVP'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank', 'o', '2.0.0'),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._schokindexMvp = OTLAttribuut(field=KlLEACSchokindexMVP,
                                           naam='schokindexMvp',
                                           label='schokindex mvp',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindexMVP.schokindexMvp',
                                           usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                           deprecated_version='2.0.0',
                                           definition='Head Injury Criterium (HIC) van een motorvangplank.',
                                           owner=self)

    @property
    def schokindexMvp(self) -> str:
        """Head Injury Criterium (HIC) van een motorvangplank."""
        return self._schokindexMvp.get_waarde()

    @schokindexMvp.setter
    def schokindexMvp(self, value):
        self._schokindexMvp.set_waarde(value, owner=self)
