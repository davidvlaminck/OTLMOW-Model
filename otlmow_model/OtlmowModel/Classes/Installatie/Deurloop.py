# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlVastAanslagmateriaal import KlVastAanslagmateriaal
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Deurloop(AIMNaamObject, VlakGeometrie):
    """Vaste uitsparing op de bodem van het constructiehoofd over de breedte van de constructie voor de waterdichting en/of krachtoverdracht van de roldeur."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Deurloop'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Sluishoofd', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._vastAanslagmateriaal = OTLAttribuut(field=KlVastAanslagmateriaal,
                                                  naam='vastAanslagmateriaal',
                                                  label='vast aanslagmateriaal',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Deurloop.vastAanslagmateriaal',
                                                  definition='De verschillende mogelijkheden m.b.t. het materiaal van de aanslag',
                                                  owner=self)

    @property
    def vastAanslagmateriaal(self) -> str:
        """De verschillende mogelijkheden m.b.t. het materiaal van de aanslag"""
        return self._vastAanslagmateriaal.get_waarde()

    @vastAanslagmateriaal.setter
    def vastAanslagmateriaal(self, value):
        self._vastAanslagmateriaal.set_waarde(value, owner=self)
