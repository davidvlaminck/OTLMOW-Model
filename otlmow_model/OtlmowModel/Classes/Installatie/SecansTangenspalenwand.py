# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Grondkeringen import Grondkeringen
from ...Classes.Abstracten.WaterremmendeFunctie import WaterremmendeFunctie
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KwantWrdInCentimeter import (
    KwantWrdInCentimeter,
    KwantWrdInCentimeterWaarden,
)
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SecansTangenspalenwand(Grondkeringen, WaterremmendeFunctie, AIMNaamObject, LijnGeometrie, VlakGeometrie):
    """Een secans- of tangenspalenwand bestaat uit betonnen boorpalen. Bij de secanspalenwand zijn dit primaire en secundaire, in elkaar oversneden palen. Bij de tangenspalenwand snijden de boorpalen niet in elkaar in (geen overlap). De wand heeft tot doel een bouwputbeschoeiing te realiseren. De stabiliteit van de grondkering wordt verzekerd door verankeringen en/of schoringen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#SecansTangenspalenwand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BalkGK', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondanker', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BetonnenBoorpaal', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CFAPaal', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._hOhAfstandPalen = OTLAttribuut(field=KwantWrdInCentimeter,
                                             naam='hOhAfstandPalen',
                                             label='h. o. h. afstand palen',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#SecansTangenspalenwand.hOhAfstandPalen',
                                             definition='Hart op hart afstand tussen palen in de wand.',
                                             owner=self)

        self._heeftInsnijdendePalen = OTLAttribuut(field=BooleanField,
                                                   naam='heeftInsnijdendePalen',
                                                   label='heeft insnijdende palen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#SecansTangenspalenwand.heeftInsnijdendePalen',
                                                   definition='Bepaling of er insnijdende palen aanwezig zijn.',
                                                   owner=self)

        self._rekennota = OTLAttribuut(field=DtcDocument,
                                       naam='rekennota',
                                       label='rekeningnota',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#SecansTangenspalenwand.rekennota',
                                       definition='De bijhorende rekennota met berekeningen.',
                                       owner=self)

    @property
    def hOhAfstandPalen(self) -> KwantWrdInCentimeterWaarden:
        """Hart op hart afstand tussen palen in de wand."""
        return self._hOhAfstandPalen.get_waarde()

    @hOhAfstandPalen.setter
    def hOhAfstandPalen(self, value):
        self._hOhAfstandPalen.set_waarde(value, owner=self)

    @property
    def heeftInsnijdendePalen(self) -> bool:
        """Bepaling of er insnijdende palen aanwezig zijn."""
        return self._heeftInsnijdendePalen.get_waarde()

    @heeftInsnijdendePalen.setter
    def heeftInsnijdendePalen(self, value):
        self._heeftInsnijdendePalen.set_waarde(value, owner=self)

    @property
    def rekennota(self) -> DtcDocumentWaarden:
        """De bijhorende rekennota met berekeningen."""
        return self._rekennota.get_waarde()

    @rekennota.setter
    def rekennota(self, value):
        self._rekennota.set_waarde(value, owner=self)
