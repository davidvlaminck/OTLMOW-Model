# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeGlijmateriaal import KlTypeGlijmateriaal
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Glijmateriaal(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een slijtagegevoelig onderdeel dat direct contact maakt met een relatief bewegend onderdeel. Het dient vooral om slijtage, wrijving of schade aan de betrokken glijoppervlakken te beperken en om krachten over te brengen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Glijmateriaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugligger', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DraagstructuurBWCTWC', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Centreervork', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rol', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Glijgeleiding', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Grendelmechanisme', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Railconstructie', 'o', None),  # o = direction: outgoing
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LigtOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Tegenmateriaal', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._typeGlijmateriaal = OTLAttribuut(field=KlTypeGlijmateriaal,
                                               naam='typeGlijmateriaal',
                                               label='type glijmateriaal',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Glijmateriaal.typeGlijmateriaal',
                                               definition='Het type glijmateriaal.',
                                               owner=self)

    @property
    def typeGlijmateriaal(self) -> str:
        """Het type glijmateriaal."""
        return self._typeGlijmateriaal.get_waarde()

    @typeGlijmateriaal.setter
    def typeGlijmateriaal(self, value):
        self._typeGlijmateriaal.set_waarde(value, owner=self)
