# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlMIVLusUitslijprichting import KlMIVLusUitslijprichting
from ...Datatypes.KlMIVLusZichtbaarheid import KlMIVLusZichtbaarheid
from ...GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVLus(AIMNaamObject, LijnGeometrie):
    """Meten in Vlaanderen : inductieve lus,ingeslepen in het wegdek."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt', 'o', '2.9.0'),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVMeetpunt', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Doorverbinddoos', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LoopTerminationAndProtection', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._meetrapport = OTLAttribuut(field=DtcDocument,
                                         naam='meetrapport',
                                         label='meetrapport',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus.meetrapport',
                                         usagenote='Attribuut uit gebruik sinds versie 2.9.0 ',
                                         deprecated_version='2.9.0',
                                         definition='De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen.',
                                         owner=self)

        self._uitslijprichting = OTLAttribuut(field=KlMIVLusUitslijprichting,
                                              naam='uitslijprichting',
                                              label='uitslijprichting',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus.uitslijprichting',
                                              usagenote='Attribuut uit gebruik sinds versie 2.9.0 ',
                                              deprecated_version='2.9.0',
                                              definition='De uitlopers van de lus gaan naar links of naar rechts bekeken ten opzichte van de rijrichting.',
                                              owner=self)

        self._zichtbaarheid = OTLAttribuut(field=KlMIVLusZichtbaarheid,
                                           naam='zichtbaarheid',
                                           label='zichtbaarheid',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus.zichtbaarheid',
                                           usagenote='Attribuut uit gebruik sinds versie 2.9.0 ',
                                           deprecated_version='2.9.0',
                                           definition='Is dus lus zichtbaar in het wegdek of bedekt door een toplaag.',
                                           owner=self)

    @property
    def meetrapport(self) -> DtcDocumentWaarden:
        """De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen."""
        return self._meetrapport.get_waarde()

    @meetrapport.setter
    def meetrapport(self, value):
        self._meetrapport.set_waarde(value, owner=self)

    @property
    def uitslijprichting(self) -> str:
        """De uitlopers van de lus gaan naar links of naar rechts bekeken ten opzichte van de rijrichting."""
        return self._uitslijprichting.get_waarde()

    @uitslijprichting.setter
    def uitslijprichting(self, value):
        self._uitslijprichting.set_waarde(value, owner=self)

    @property
    def zichtbaarheid(self) -> str:
        """Is dus lus zichtbaar in het wegdek of bedekt door een toplaag."""
        return self._zichtbaarheid.get_waarde()

    @zichtbaarheid.setter
    def zichtbaarheid(self, value):
        self._zichtbaarheid.set_waarde(value, owner=self)
