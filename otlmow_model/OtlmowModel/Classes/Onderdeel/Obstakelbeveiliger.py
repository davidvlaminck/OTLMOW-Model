# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.AfschermendeConstructie import AfschermendeConstructie
from ...Classes.Abstracten.SchokindexVoertuigkering import SchokindexVoertuigkering
from ...Datatypes.KlLEACObstakelbeveiligerType import KlLEACObstakelbeveiligerType
from ...Datatypes.KlLEACPerformantieniveau import KlLEACPerformantieniveau
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Obstakelbeveiliger(AfschermendeConstructie, SchokindexVoertuigkering, VlakGeometrie):
    """Een energie-absorberende constructie voor voertuigen,geïnstalleerd vóór één of meerdere obstakels,met als doel de ernst van een botsing te reduceren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieniveau', 'i', '2.0.0'),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindex', 'i', '2.0.0'),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie', 'i', None),  # i = direction: incoming
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._performantieniveau = OTLAttribuut(field=KlLEACPerformantieniveau,
                                                naam='performantieniveau',
                                                label='performantieniveau',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger.performantieniveau',
                                                definition='Het niveau waarop de obstakelbeveiliger is getest.',
                                                owner=self)

        self._type = OTLAttribuut(field=KlLEACObstakelbeveiligerType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger.type',
                                  definition='De functie die de obstakelbeveiliger vervult.',
                                  owner=self)

    @property
    def performantieniveau(self) -> str:
        """Het niveau waarop de obstakelbeveiliger is getest."""
        return self._performantieniveau.get_waarde()

    @performantieniveau.setter
    def performantieniveau(self, value):
        self._performantieniveau.set_waarde(value, owner=self)

    def _get_type(self) -> str:
        """De functie die de obstakelbeveiliger vervult."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
