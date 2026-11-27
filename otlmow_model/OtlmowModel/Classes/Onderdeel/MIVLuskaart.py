# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlMIVLuskaartType import KlMIVLuskaartType
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVLuskaart(AIMNaamObject, PuntGeometrie):
    """Meten in Vlaanderen : kaart in LVE- of SAT- rack met de analoge circuits voor de lussen en analoog/digitaal conversie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie', 'o', '2.9.0'),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LoopTerminationAndProtection', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVCommunicatiekaart', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._lussenMeetrapport = OTLAttribuut(field=DtcDocument,
                                               naam='lussenMeetrapport',
                                               label='lussen meetrapport',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart.lussenMeetrapport',
                                               usagenote='Bestanden van het type pdf.',
                                               definition='De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen.',
                                               owner=self)

        self._type = OTLAttribuut(field=KlMIVLuskaartType,
                                  naam='type',
                                  label='type MIV luskaart',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart.type',
                                  definition='De uitvoering van de luskaart volgens een vaste lijst van mogelijke types.',
                                  owner=self)

    @property
    def lussenMeetrapport(self) -> DtcDocumentWaarden:
        """De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen."""
        return self._lussenMeetrapport.get_waarde()

    @lussenMeetrapport.setter
    def lussenMeetrapport(self, value):
        self._lussenMeetrapport.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """De uitvoering van de luskaart volgens een vaste lijst van mogelijke types."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
