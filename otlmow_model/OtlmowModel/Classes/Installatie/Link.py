# coding=utf-8
from typing import ClassVar

from ...BaseClasses.IntegerField import IntegerField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...BaseClasses.StringField import StringField
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlNetwerklinkMediumtype import KlNetwerklinkMediumtype
from ...GeometrieTypes.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Link(NaampadObject, GeenGeometrie):
    """Het (glasvezel) traject tussen twee toestellen (NetwerkElementen) die rechtstreeks met mekaar communiceren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Been', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._geleidingsgroepTnummer = OTLAttribuut(field=IntegerField,
                                                    naam='geleidingsgroepTnummer',
                                                    label='geleidingsgroep T-nummer',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link.geleidingsgroepTnummer',
                                                    definition='T-nummer van de geleidingsgroep in de kabelnet toepassing.',
                                                    owner=self)

        self._mediumtype = OTLAttribuut(field=KlNetwerklinkMediumtype,
                                        naam='mediumtype',
                                        label='mediumtype',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link.mediumtype',
                                        definition='Geeft aan hoe de verbinding tussen Netwerkelementen fysiek gerealiseerd wordt',
                                        owner=self)

        self._ring = OTLAttribuut(field=StringField,
                                  naam='ring',
                                  label='ring',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link.ring',
                                  definition='Naam van de ringstructuur in het transport netwerk.',
                                  owner=self)

    @property
    def geleidingsgroepTnummer(self) -> int:
        """T-nummer van de geleidingsgroep in de kabelnet toepassing."""
        return self._geleidingsgroepTnummer.get_waarde()

    @geleidingsgroepTnummer.setter
    def geleidingsgroepTnummer(self, value):
        self._geleidingsgroepTnummer.set_waarde(value, owner=self)

    @property
    def mediumtype(self) -> str:
        """Geeft aan hoe de verbinding tussen Netwerkelementen fysiek gerealiseerd wordt"""
        return self._mediumtype.get_waarde()

    @mediumtype.setter
    def mediumtype(self, value):
        self._mediumtype.set_waarde(value, owner=self)

    @property
    def ring(self) -> str:
        """Naam van de ringstructuur in het transport netwerk."""
        return self._ring.get_waarde()

    @ring.setter
    def ring(self, value):
        self._ring.set_waarde(value, owner=self)
