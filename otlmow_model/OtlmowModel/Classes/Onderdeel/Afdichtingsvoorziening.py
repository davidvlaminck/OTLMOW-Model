# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlAfdichtingsvoorzieningtype import KlAfdichtingsvoorzieningtype
from ...Datatypes.KlMateriaalAfdichtingsvoorziening import (
    KlMateriaalAfdichtingsvoorziening,
)
from ...Datatypes.KwantWrdInMeter import KwantWrdInMeter, KwantWrdInMeterWaarden
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afdichtingsvoorziening(AIMNaamObject, PuntGeometrie):
    """Een afdichtingsvoorziening is een afdichtend component dat wordt toegepast ter hoogte van een voeg, naad of overgang tussen constructiedelen om waterdichtheid te realiseren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichtingsvoorziening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aanslagbalk', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kokervoeg', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BeweegbareWaterkerendeConstructie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeWaterkerendeConstructie', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichtingsvoorziening.lengte',
                                    definition='De lengte van de afdichtingsvoorziening, uitgedrukt in meter',
                                    owner=self)

        self._materiaalAfdichtingsvoorziening = OTLAttribuut(field=KlMateriaalAfdichtingsvoorziening,
                                                             naam='materiaalAfdichtingsvoorziening',
                                                             label='materiaal afdichtingsvoorziening',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichtingsvoorziening.materiaalAfdichtingsvoorziening',
                                                             definition='De verschillende materialen die worden gebruikt voor het maken van afdichtingsvoorzieningen.',
                                                             owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichtingsvoorziening.technischeFiche',
                                             definition='De technische fiche van de afdichtingsvoorziening.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlAfdichtingsvoorzieningtype,
                                  naam='type',
                                  label='type afdichtingsvoorziening',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichtingsvoorziening.type',
                                  definition='De verschillende types afdichtingsvoorzieningen.',
                                  owner=self)

    @property
    def lengte(self) -> KwantWrdInMeterWaarden:
        """De lengte van de afdichtingsvoorziening, uitgedrukt in meter"""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def materiaalAfdichtingsvoorziening(self) -> str:
        """De verschillende materialen die worden gebruikt voor het maken van afdichtingsvoorzieningen."""
        return self._materiaalAfdichtingsvoorziening.get_waarde()

    @materiaalAfdichtingsvoorziening.setter
    def materiaalAfdichtingsvoorziening(self, value):
        self._materiaalAfdichtingsvoorziening.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de afdichtingsvoorziening."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """De verschillende types afdichtingsvoorzieningen."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
