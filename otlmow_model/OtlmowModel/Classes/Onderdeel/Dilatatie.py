# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from ...Datatypes.KlLEACUitzettingswaardeDilatatie import (
    KlLEACUitzettingswaardeDilatatie,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dilatatie(AIMObject, PuntGeometrie):
    """Dilataties zijn bedoeld om ervoor te zorgen dat geleideconstructies vrij kunnen krimpen en uitzetten bij onder andere temperatuurwisselingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dilatatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._uitzettingswaarde = OTLAttribuut(field=KlLEACUitzettingswaardeDilatatie,
                                               naam='uitzettingswaarde',
                                               label='uitzettingswaarde',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dilatatie.uitzettingswaarde',
                                               definition='De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing.',
                                               owner=self)

    @property
    def uitzettingswaarde(self) -> str:
        """De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing."""
        return self._uitzettingswaarde.get_waarde()

    @uitzettingswaarde.setter
    def uitzettingswaarde(self, value):
        self._uitzettingswaarde.set_waarde(value, owner=self)
