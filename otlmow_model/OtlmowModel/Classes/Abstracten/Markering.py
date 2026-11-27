# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Signalisatie import Signalisatie
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.DtcMarkeringOpvatting import (
    DtcMarkeringOpvatting,
    DtcMarkeringOpvattingWaarden,
)
from ...Datatypes.DtcProductidentificatiecode import (
    DtcProductidentificatiecode,
    DtcProductidentificatiecodeWaarden,
)
from ...Datatypes.KlKleurMarkering import KlKleurMarkering
from ...Datatypes.KlMarkeringSoort import KlMarkeringSoort
from ...Datatypes.KlMarkeringsproduct import KlMarkeringsproduct
from ...Datatypes.KlMarkeringssysteem import KlMarkeringssysteem


# Generated with OTLClassCreator. To modify: extend, do not edit
class Markering(Signalisatie, AIMObject):
    """Abstracte als noemer voor de verschillende types van markeringen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereLaag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AndereVerharding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ArtificieleLaag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LaagBouwklasse', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afdichting', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Asfaltmat', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BeschermingWapening', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Beschermlaag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetontegel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGebakkenStraatsteen', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanGrasbetontegel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanKassei', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanNatuursteentegel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bestrijking', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Betonmat', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Betonmatras', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cementbetonverharding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ColloidaalBeton', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dolomietverharding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draineerlaag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DrukspreidendeConstructie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DunneOverlaging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeexpandeerdPolystyreen', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geotextiel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grond', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Noppendrainage', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OnbegroeidVoorkomen', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderbouw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ScheurremmendeLaag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Slemlaag', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Steenslagverharding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortdraad', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ternairmengselverharding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerhardingGrasKunststofplaat', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Walsbetonverharding', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wiepenmat', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefLuminantie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefStroefheid', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijDagOfWV', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNacht', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNachtNatWegdek', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefZichtbaarheidBijNachtRegenweer', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._isHandwerk = OTLAttribuut(field=BooleanField,
                                        naam='isHandwerk',
                                        label='is handwerk',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.isHandwerk',
                                        definition='Boolean om te bepalen of de markering machinaal of handmatig is aangebracht.',
                                        owner=self)

        self._isTijdelijk = OTLAttribuut(field=BooleanField,
                                         naam='isTijdelijk',
                                         label='is tijdelijk',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.isTijdelijk',
                                         definition='Aanduiding of de wegmarkering al dan niet tot de werfsignalisatie behoort.',
                                         owner=self)

        self._kleur = OTLAttribuut(field=KlKleurMarkering,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.kleur',
                                   definition='De kleur van de gebruikte markering.',
                                   owner=self)

        self._markeringsoort = OTLAttribuut(field=KlMarkeringSoort,
                                            naam='markeringsoort',
                                            label='markeringsoort',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.markeringsoort',
                                            usagenote='Attribuut uit gebruik sinds versie 2.18.0 ',
                                            deprecated_version='2.18.0',
                                            definition='De soort van markering (verf, thermopast,...).',
                                            owner=self)

        self._markeringsproduct = OTLAttribuut(field=KlMarkeringsproduct,
                                               naam='markeringsproduct',
                                               label='markeringsproduct',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.markeringsproduct',
                                               definition='Het type product van de markering.',
                                               owner=self)

        self._markeringssysteem = OTLAttribuut(field=KlMarkeringssysteem,
                                               naam='markeringssysteem',
                                               label='markeringssysteem',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.markeringssysteem',
                                               definition='Een combinatie van een markeringsproduct en één of meer soorten glasparels of een geschikt mengsel van glasparels en een stroefmakend middel, aangebracht met een welbepaalde methode en met een welbepaalde dosering.',
                                               owner=self)

        self._markeringsysteemCopro = OTLAttribuut(field=DtcProductidentificatiecode,
                                                   naam='markeringsysteemCopro',
                                                   label='markeringsysteem COPRO',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.markeringsysteemCopro',
                                                   definition='De product informatie van de markering via COPRO codes.',
                                                   owner=self)

        self._opvatting = OTLAttribuut(field=DtcMarkeringOpvatting,
                                       naam='opvatting',
                                       label='opvatting',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.opvatting',
                                       definition='De opvatting van de markering, zijnde middelenverbintenis of resultaatsverbintenis met een minimale levensduur.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche(s) van de markering.',
                                             owner=self)

    @property
    def isHandwerk(self) -> bool:
        """Boolean om te bepalen of de markering machinaal of handmatig is aangebracht."""
        return self._isHandwerk.get_waarde()

    @isHandwerk.setter
    def isHandwerk(self, value):
        self._isHandwerk.set_waarde(value, owner=self)

    @property
    def isTijdelijk(self) -> bool:
        """Aanduiding of de wegmarkering al dan niet tot de werfsignalisatie behoort."""
        return self._isTijdelijk.get_waarde()

    @isTijdelijk.setter
    def isTijdelijk(self, value):
        self._isTijdelijk.set_waarde(value, owner=self)

    @property
    def kleur(self) -> str:
        """De kleur van de gebruikte markering."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def markeringsoort(self) -> str:
        """De soort van markering (verf, thermopast,...)."""
        return self._markeringsoort.get_waarde()

    @markeringsoort.setter
    def markeringsoort(self, value):
        self._markeringsoort.set_waarde(value, owner=self)

    @property
    def markeringsproduct(self) -> str:
        """Het type product van de markering."""
        return self._markeringsproduct.get_waarde()

    @markeringsproduct.setter
    def markeringsproduct(self, value):
        self._markeringsproduct.set_waarde(value, owner=self)

    @property
    def markeringssysteem(self) -> str:
        """Een combinatie van een markeringsproduct en één of meer soorten glasparels of een geschikt mengsel van glasparels en een stroefmakend middel, aangebracht met een welbepaalde methode en met een welbepaalde dosering."""
        return self._markeringssysteem.get_waarde()

    @markeringssysteem.setter
    def markeringssysteem(self, value):
        self._markeringssysteem.set_waarde(value, owner=self)

    @property
    def markeringsysteemCopro(self) -> DtcProductidentificatiecodeWaarden:
        """De product informatie van de markering via COPRO codes."""
        return self._markeringsysteemCopro.get_waarde()

    @markeringsysteemCopro.setter
    def markeringsysteemCopro(self, value):
        self._markeringsysteemCopro.set_waarde(value, owner=self)

    @property
    def opvatting(self) -> DtcMarkeringOpvattingWaarden:
        """De opvatting van de markering, zijnde middelenverbintenis of resultaatsverbintenis met een minimale levensduur."""
        return self._opvatting.get_waarde()

    @opvatting.setter
    def opvatting(self, value):
        self._opvatting.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> list[DtcDocumentWaarden]:
        """De technische fiche(s) van de markering."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
