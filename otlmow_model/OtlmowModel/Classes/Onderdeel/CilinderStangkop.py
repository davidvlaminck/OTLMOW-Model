# coding=utf-8
from typing import ClassVar

from ...BaseClasses.BooleanField import BooleanField
from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class CilinderStangkop(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Het mechanisch onderdeel (oog of vork) dat op het uiteinde van de cilinderstang wordt gemonteerd en de verbinding van de stang met de bewegende constructie realiseert."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CilinderStangkop'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AsLagerCombinatie', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cilinderstang', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pen', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Cilindermechanisme', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._isOog = OTLAttribuut(field=BooleanField,
                                   naam='isOog',
                                   label='is oog',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CilinderStangkop.isOog',
                                   definition='Geeft aan of de stangkop uitgevoerd is als oog. In zo een geval wordt de stangkop tussen een gaffel geschoven. In het andere geval is de stangkop zelf een gaffel dat over een oog wordt geschoven.',
                                   owner=self)

    @property
    def isOog(self) -> bool:
        """Geeft aan of de stangkop uitgevoerd is als oog. In zo een geval wordt de stangkop tussen een gaffel geschoven. In het andere geval is de stangkop zelf een gaffel dat over een oog wordt geschoven."""
        return self._isOog.get_waarde()

    @isOog.setter
    def isOog(self, value):
        self._isOog.set_waarde(value, owner=self)
