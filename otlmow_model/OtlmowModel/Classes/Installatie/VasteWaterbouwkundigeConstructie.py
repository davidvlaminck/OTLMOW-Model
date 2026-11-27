# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlVWCTypeNivelleringssysteem import KlVWCTypeNivelleringssysteem
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VasteWaterbouwkundigeConstructie(AIMNaamObject, VlakGeometrie):
    """Statische bouwkundige constructie in of aan een waterloop al dan niet in combinatie met een beweegbare waterkerende constructie, om grond en een waterpeilverschil te keren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorigheidSluisStuw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Constructiehoofd', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelkoker', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolk', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Omloopriool', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluis', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Stuw', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._heeftPompput = OTLAttribuut(field=BooleanField,
                                          naam='heeftPompput',
                                          label='heeft pompput',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie.heeftPompput',
                                          definition='Geeft aan of de vaste waterbouwkundige constructie een pompput heeft.',
                                          owner=self)

        self._heeftWoelkamer = OTLAttribuut(field=BooleanField,
                                            naam='heeftWoelkamer',
                                            label='heeft woelkamer',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie.heeftWoelkamer',
                                            definition='Geeft aan of er al dan niet een woelkamer aanwezig is in de vaste waterbouwkundige constructie.',
                                            owner=self)

        self._typeNivelleringssysteem = OTLAttribuut(field=KlVWCTypeNivelleringssysteem,
                                                     naam='typeNivelleringssysteem',
                                                     label='type nivelleringssysteem',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VasteWaterbouwkundigeConstructie.typeNivelleringssysteem',
                                                     definition='Verwijst naar het type systeem dat gebruikt wordt voor de nivellering in vaste waterbouwkundige constructies.',
                                                     owner=self)

    @property
    def heeftPompput(self) -> bool:
        """Geeft aan of de vaste waterbouwkundige constructie een pompput heeft."""
        return self._heeftPompput.get_waarde()

    @heeftPompput.setter
    def heeftPompput(self, value):
        self._heeftPompput.set_waarde(value, owner=self)

    @property
    def heeftWoelkamer(self) -> bool:
        """Geeft aan of er al dan niet een woelkamer aanwezig is in de vaste waterbouwkundige constructie."""
        return self._heeftWoelkamer.get_waarde()

    @heeftWoelkamer.setter
    def heeftWoelkamer(self, value):
        self._heeftWoelkamer.set_waarde(value, owner=self)

    @property
    def typeNivelleringssysteem(self) -> str:
        """Verwijst naar het type systeem dat gebruikt wordt voor de nivellering in vaste waterbouwkundige constructies."""
        return self._typeNivelleringssysteem.get_waarde()

    @typeNivelleringssysteem.setter
    def typeNivelleringssysteem(self, value):
        self._typeNivelleringssysteem.set_waarde(value, owner=self)
