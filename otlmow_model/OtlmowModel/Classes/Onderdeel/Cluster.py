# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...Datatypes.KlClusterClusterdoel import KlClusterClusterdoel
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cluster(NaampadObject, PuntGeometrie):
    """Groep van servers die samenwerken om een gemeenschappelijk doel te bereiken (zowel voor groeperen van resources en/of redundantie)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hardware', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWGehostOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsSWGehostOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer', 'i', None),  # i = direction: incoming
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._clusterdoel = OTLAttribuut(field=KlClusterClusterdoel,
                                         naam='clusterdoel',
                                         label='clusterdoel',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cluster.clusterdoel',
                                         definition='De reden waarom de custer is opgezet, bv. resources groeperen of redundantie.',
                                         owner=self)

    @property
    def clusterdoel(self) -> str:
        """De reden waarom de custer is opgezet, bv. resources groeperen of redundantie."""
        return self._clusterdoel.get_waarde()

    @clusterdoel.setter
    def clusterdoel(self, value):
        self._clusterdoel.set_waarde(value, owner=self)
