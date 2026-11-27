# coding=utf-8
from abc import abstractmethod
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.ArtificieleLaag import ArtificieleLaag
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlBestratingSteenverband import KlBestratingSteenverband
from ...Datatypes.KlBestratingVoegvulling import KlBestratingVoegvulling
from ...Datatypes.KlKleurSupp import KlKleurSupp


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bestrating(ArtificieleLaag):
    """Verhardingstype opgebouwd uit bestratingen (rechthoekige of vierkante componenten van beperkte afmetingen) waardoor een aanzienlijk aantal voegen tussen de componenten zitten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDoorlatendheid', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVlakheid', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', 'i', None),  # i = direction: incoming
    ]

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._kleur = OTLAttribuut(field=KlKleurSupp,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating.kleur',
                                   definition='De kleur van de bestrating.',
                                   owner=self)

        self._steenverband = OTLAttribuut(field=KlBestratingSteenverband,
                                          naam='steenverband',
                                          label='steenverband',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating.steenverband',
                                          definition='Het patroon waarin de bestrating gelegd werd.',
                                          owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de bestrating.',
                                             owner=self)

        self._voegvulling = OTLAttribuut(field=KlBestratingVoegvulling,
                                         naam='voegvulling',
                                         label='voegvulling',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Bestrating.voegvulling',
                                         definition='De gebruikte voegvulling van de bestrating.',
                                         owner=self)

    @property
    def kleur(self) -> str:
        """De kleur van de bestrating."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def steenverband(self) -> str:
        """Het patroon waarin de bestrating gelegd werd."""
        return self._steenverband.get_waarde()

    @steenverband.setter
    def steenverband(self, value):
        self._steenverband.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> list[DtcDocumentWaarden]:
        """De technische fiche van de bestrating."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def voegvulling(self) -> str:
        """De gebruikte voegvulling van de bestrating."""
        return self._voegvulling.get_waarde()

    @voegvulling.setter
    def voegvulling(self, value):
        self._voegvulling.set_waarde(value, owner=self)
