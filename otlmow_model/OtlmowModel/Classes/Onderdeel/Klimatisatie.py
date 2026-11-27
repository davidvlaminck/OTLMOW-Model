# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlKlimatisatieMerk import KlKlimatisatieMerk
from ...Datatypes.KlKlimatisatieModelnaam import KlKlimatisatieModelnaam
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Klimatisatie(NaampadObject, PuntGeometrie):
    """Component waarmee de temperatuur en klimaat geregeld wordt van het objecttype waaraan het bevestigd is zoals een behuizing of ruimte."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._merk = OTLAttribuut(field=KlKlimatisatieMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie.merk',
                                  definition='De merknaam van de klimatisatie volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlKlimatisatieModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie.modelnaam',
                                       definition='Naam waarmee de fabrikant het model van de klimatisatie identificeert.',
                                       owner=self)

    @property
    def merk(self) -> str:
        """De merknaam van de klimatisatie volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self) -> str:
        """Naam waarmee de fabrikant het model van de klimatisatie identificeert."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
