# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AndereVerharding import AndereVerharding
from ...Datatypes.DtcDocument import DtcDocument, DtcDocumentWaarden
from ...Datatypes.KlSchanskorfVorm import KlSchanskorfVorm
from ...Datatypes.KlStortsteenKaliber import KlStortsteenKaliber
from ...Datatypes.KlStortsteenType import KlStortsteenType
from ...Datatypes.KlTypeSchanskorf import KlTypeSchanskorf


# Generated with OTLClassCreator. To modify: extend, do not edit
class Schanskorf(AndereVerharding):
    """Een schanskorf bestaat uit een metalen gaasnet dat wordt gevuld met steenachtige materialen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GewapendeGrond', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._heeftVerankeringspalen = OTLAttribuut(field=BooleanField,
                                                    naam='heeftVerankeringspalen',
                                                    label='heeft verankeringspalen',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.heeftVerankeringspalen',
                                                    definition='Aanduiding of de palen de functie hebben om een schanskorf te verankeren.',
                                                    owner=self)

        self._isGegalvaniseerd = OTLAttribuut(field=BooleanField,
                                              naam='isGegalvaniseerd',
                                              label='is gegalvaniseerd',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.isGegalvaniseerd',
                                              definition='Aanduiding of de schanskorf gegalvaniseerd is.',
                                              owner=self)

        self._isGelast = OTLAttribuut(field=BooleanField,
                                      naam='isGelast',
                                      label='is gelast',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.isGelast',
                                      definition='Aanduiding of de schanskorf gelast is.',
                                      owner=self)

        self._kaliber = OTLAttribuut(field=KlStortsteenKaliber,
                                     naam='kaliber',
                                     label='kaliber',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.kaliber',
                                     definition='Het kaliber of gemiddelde diameter van de stenen in de schanskorf.',
                                     owner=self)

        self._materiaalVulling = OTLAttribuut(field=KlStortsteenType,
                                              naam='materiaalVulling',
                                              label='materiaalvulling',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.materiaalVulling',
                                              definition='Het soort stenen waaruit de opvulling van een schanskorf bestaat.',
                                              owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de schanskorven als bijlage.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlTypeSchanskorf,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.type',
                                  definition='Duidt het type schanskorf aan.',
                                  owner=self)

        self._vorm = OTLAttribuut(field=KlSchanskorfVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.vorm',
                                  definition='De gebruikte vorm van de schanskorf.',
                                  owner=self)

    @property
    def heeftVerankeringspalen(self) -> bool:
        """Aanduiding of de palen de functie hebben om een schanskorf te verankeren."""
        return self._heeftVerankeringspalen.get_waarde()

    @heeftVerankeringspalen.setter
    def heeftVerankeringspalen(self, value):
        self._heeftVerankeringspalen.set_waarde(value, owner=self)

    @property
    def isGegalvaniseerd(self) -> bool:
        """Aanduiding of de schanskorf gegalvaniseerd is."""
        return self._isGegalvaniseerd.get_waarde()

    @isGegalvaniseerd.setter
    def isGegalvaniseerd(self, value):
        self._isGegalvaniseerd.set_waarde(value, owner=self)

    @property
    def isGelast(self) -> bool:
        """Aanduiding of de schanskorf gelast is."""
        return self._isGelast.get_waarde()

    @isGelast.setter
    def isGelast(self, value):
        self._isGelast.set_waarde(value, owner=self)

    @property
    def kaliber(self) -> str:
        """Het kaliber of gemiddelde diameter van de stenen in de schanskorf."""
        return self._kaliber.get_waarde()

    @kaliber.setter
    def kaliber(self, value):
        self._kaliber.set_waarde(value, owner=self)

    @property
    def materiaalVulling(self) -> str:
        """Het soort stenen waaruit de opvulling van een schanskorf bestaat."""
        return self._materiaalVulling.get_waarde()

    @materiaalVulling.setter
    def materiaalVulling(self, value):
        self._materiaalVulling.set_waarde(value, owner=self)

    @property
    def technischeFiche(self) -> list[DtcDocumentWaarden]:
        """De technische fiche van de schanskorven als bijlage."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """Duidt het type schanskorf aan."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)

    @property
    def vorm(self) -> str:
        """De gebruikte vorm van de schanskorf."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
