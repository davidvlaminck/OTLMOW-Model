# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.VRIDraagconstructie import VRIDraagconstructie
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlRechteSteunType import KlRechteSteunType
from ...Datatypes.KwantWrdInMillimeter import (
    KwantWrdInMillimeter,
    KwantWrdInMillimeterWaarden,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class RechteSteun(VRIDraagconstructie, NaampadObject, PuntGeometrie):
    """Rechte paal voor het steun geven aan allerlei installaties. Dit omvat het volledige draagsysteem, zijnde de logische samenstelling van met elkaar verbonden onderdelen, bestemd voor het geven van mechanische sterkte en stabiliteit aan de installatie voor wegsignalering."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RechteSteun'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verkeersbord', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ZenderOntvangerToegang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Gebouw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ForfaitaireAansluiting', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BiFlashInstallatie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokerafsluiting', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VRIBuiteninstallatie', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._doorsnede = OTLAttribuut(field=KwantWrdInMillimeter,
                                       naam='doorsnede',
                                       label='diameter',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RechteSteun.doorsnede',
                                       definition='De doorsnede of diameter van de rechte steun, uitgedrukt in millimeter.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RechteSteun.technischeFiche',
                                             definition='De technische fiche van de rechte steun.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlRechteSteunType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RechteSteun.type',
                                  definition='Het type verwijst naar de aanpassingen die gebeuren wanneer een andere techniek gebruik maakt van de rechte steun. Meestal gaat dit over een aanpassing in de lengte van het verjongde deel van de rechte steun.',
                                  owner=self)

    @property
    def doorsnede(self) -> KwantWrdInMillimeterWaarden:
        """De doorsnede of diameter van de rechte steun, uitgedrukt in millimeter."""
        return self._doorsnede.get_waarde()

    @doorsnede.setter
    def doorsnede(self, value):
        self._doorsnede.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> DtcDocumentWaarden:
        """De technische fiche van de rechte steun."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Het type verwijst naar de aanpassingen die gebeuren wanneer een andere techniek gebruik maakt van de rechte steun. Meestal gaat dit over een aanpassing in de lengte van het verjongde deel van de rechte steun."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
