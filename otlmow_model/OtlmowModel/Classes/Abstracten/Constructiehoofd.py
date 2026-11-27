# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Datatypes.KlVWCDroogzetbaarheid import KlVWCDroogzetbaarheid
from ...Datatypes.KwantWrdInCentimeter import (
    KwantWrdInCentimeter,
    KwantWrdInCentimeterWaarden,
)
from ...Datatypes.KwantWrdInMeterTAW import (
    KwantWrdInMeterTAW,
    KwantWrdInMeterTAWWaarden,
)
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Constructiehoofd(VlakGeometrie):
    """Abstracte om eigenschappen en relaties te bundelen voor sluishoofd en stuwhoofd"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Constructiehoofd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorigheidSluisStuw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondkeringen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BeweegbareWaterkerendeConstructie', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._diepteSponning = OTLAttribuut(field=KwantWrdInCentimeter,
                                            naam='diepteSponning',
                                            label='diepte van de sponning',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Constructiehoofd.diepteSponning',
                                            definition='Breedte van de oplegtand tov de sponning, uitgedrukt in centimeter.',
                                            owner=self)

        self._drempelpeil = OTLAttribuut(field=KwantWrdInMeterTAW,
                                         naam='drempelpeil',
                                         label='drempelpeil',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Constructiehoofd.drempelpeil',
                                         definition='Het peil van het laagste element van de vaste constructie van de constructiehoofd, uitgedrukt in mTAW.',
                                         owner=self)

        self._droogzetbaarheid = OTLAttribuut(field=KlVWCDroogzetbaarheid,
                                              naam='droogzetbaarheid',
                                              label='droogzetbaarheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Constructiehoofd.droogzetbaarheid',
                                              definition='De verschillende mogelijkheden m.b.t. droogzetbaarheid van het constructiehoofd.',
                                              owner=self)

        self._heeftKelder = OTLAttribuut(field=BooleanField,
                                         naam='heeftKelder',
                                         label='heeft Kelder',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Constructiehoofd.heeftKelder',
                                         definition='Geeft aan of er een kelder aanwezig is.',
                                         owner=self)

    @property
    def diepteSponning(self) -> KwantWrdInCentimeterWaarden:
        """Breedte van de oplegtand tov de sponning, uitgedrukt in centimeter."""
        return self._diepteSponning.get_waarde()

    @diepteSponning.setter
    def diepteSponning(self, value):
        self._diepteSponning.set_waarde(value, owner=self)

    @property
    def drempelpeil(self) -> KwantWrdInMeterTAWWaarden:
        """Het peil van het laagste element van de vaste constructie van de constructiehoofd, uitgedrukt in mTAW."""
        return self._drempelpeil.get_waarde()

    @drempelpeil.setter
    def drempelpeil(self, value):
        self._drempelpeil.set_waarde(value, owner=self)

    @property
    def droogzetbaarheid(self) -> str:
        """De verschillende mogelijkheden m.b.t. droogzetbaarheid van het constructiehoofd."""
        return self._droogzetbaarheid.get_waarde()

    @droogzetbaarheid.setter
    def droogzetbaarheid(self, value):
        self._droogzetbaarheid.set_waarde(value, owner=self)

    @property
    def heeftKelder(self) -> bool:
        """Geeft aan of er een kelder aanwezig is."""
        return self._heeftKelder.get_waarde()

    @heeftKelder.setter
    def heeftKelder(self, value):
        self._heeftKelder.set_waarde(value, owner=self)
