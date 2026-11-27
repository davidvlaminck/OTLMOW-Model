# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.Constructiehoofd import Constructiehoofd
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlHoofdtype import KlHoofdtype


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sluishoofd(Constructiehoofd, AIMNaamObject):
    """Constructiehoofd van een sluis waarin één of meerdere sluisdeuren zitten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluishoofd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AanhorigheidSluisStuw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Grondkeringen', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#UitsparingSluisdeur', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Deurloop', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Drempel', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vloernis', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._typeHoofd = OTLAttribuut(field=KlHoofdtype,
                                       naam='typeHoofd',
                                       label='type Hoofd',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluishoofd.typeHoofd',
                                       definition='Geeft het type hoofd aan van het constructiehoofd.',
                                       owner=self)

    @property
    def typeHoofd(self) -> str:
        """Geeft het type hoofd aan van het constructiehoofd."""
        return self._typeHoofd.get_waarde()

    @typeHoofd.setter
    def typeHoofd(self, value):
        self._typeHoofd.set_waarde(value, owner=self)
