# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.LaagBouwklasse import LaagBouwklasse
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.DtuBVLaagtypes import DtuBVLaagtypes, DtuBVLaagtypesWaarden
from ...Datatypes.KlBVBindmiddel import KlBVBindmiddel
from ...Datatypes.KlBVMengseltype import KlBVMengseltype
from ...Datatypes.KlKleurSupp import KlKleurSupp


# Generated with OTLClassCreator. To modify: extend, do not edit
class BitumineuzeLaag(LaagBouwklasse, NaampadObject):
    """Flexibele verharding die meestal uit bitumineus gebonden materialen (asfalt of gietasfalt) bestaat en laagsgewijs wordt aangelegd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegdekvoeg', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegreflector', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraineervermogen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDwarsvlakheid', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefEffectiefBindmiddelgehalte', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefGemetenDikte', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKorrelverdeling', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPctHolleruimte', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRolgeluid', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTemperatuur', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefTextuurdiepte', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefVlakheid', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Hoppinzuil', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Laag', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#VegetatieElement', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._bindmiddelType = OTLAttribuut(field=KlBVBindmiddel,
                                            naam='bindmiddelType',
                                            label='bindmiddel type',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.bindmiddelType',
                                            definition='Het bindmiddeltype van de bitumineuze laag.',
                                            owner=self)

        self._kleur = OTLAttribuut(field=KlKleurSupp,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.kleur',
                                   definition='De kleur van de bitumineuze laag.',
                                   owner=self)

        self._laagtype = OTLAttribuut(field=DtuBVLaagtypes,
                                      naam='laagtype',
                                      label='laagtype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.laagtype',
                                      definition='Het type van bitumineuze laag.',
                                      owner=self)

        self._mengseltype = OTLAttribuut(field=KlBVMengseltype,
                                         naam='mengseltype',
                                         label='mengseltype',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BitumineuzeLaag.mengseltype',
                                         definition='Het type van het (giet)asfaltmengsel.',
                                         owner=self)

    @property
    def bindmiddelType(self) -> str:
        """Het bindmiddeltype van de bitumineuze laag."""
        return self._bindmiddelType.get_waarde()

    @bindmiddelType.setter
    def bindmiddelType(self, value):
        self._bindmiddelType.set_waarde(value, owner=self)

    @property
    def kleur(self) -> str:
        """De kleur van de bitumineuze laag."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def laagtype(self) -> DtuBVLaagtypesWaarden:
        """Het type van bitumineuze laag."""
        return self._laagtype.get_waarde()

    @laagtype.setter
    def laagtype(self, value):
        self._laagtype.set_waarde(value, owner=self)

    @property
    def mengseltype(self) -> str:
        """Het type van het (giet)asfaltmengsel."""
        return self._mengseltype.get_waarde()

    @mengseltype.setter
    def mengseltype(self, value):
        self._mengseltype.set_waarde(value, owner=self)
