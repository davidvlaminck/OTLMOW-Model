# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlTypeAnkerplaat import KlTypeAnkerplaat
from ...Datatypes.KwantWrdInKiloNewton import (
    KwantWrdInKiloNewton,
    KwantWrdInKiloNewtonWaarden,
)
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ankerplaat(StaalsoortObject, TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een plaat die in de grond is geplaatst of ingebetonneerd en dient om een mechanisch element, zoals een draagstoel, te positioneren en zijn krachten over te dragen aan de omliggende beton- of grondconstructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ankerplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Draagstoel', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Portiek', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schommeljuk', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._kracht = OTLAttribuut(field=KwantWrdInKiloNewton,
                                    naam='kracht',
                                    label='kracht',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ankerplaat.kracht',
                                    definition='Dit is de voorspankracht in het geval van voorgespannen ankers met tegenplaat en maximale trekkracht in het geval van ingestorte ankers of niet-ingestorte ankers.',
                                    owner=self)

        self._typeAnkerplaat = OTLAttribuut(field=KlTypeAnkerplaat,
                                            naam='typeAnkerplaat',
                                            label='type ankerplaat',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ankerplaat.typeAnkerplaat',
                                            definition='Geeft het type van ankerplaat aan.',
                                            owner=self)

    @property
    def kracht(self) -> KwantWrdInKiloNewtonWaarden:
        """Dit is de voorspankracht in het geval van voorgespannen ankers met tegenplaat en maximale trekkracht in het geval van ingestorte ankers of niet-ingestorte ankers."""
        return self._kracht.get_waarde()

    @kracht.setter
    def kracht(self, value):
        self._kracht.set_waarde(value, owner=self)

    @property
    def typeAnkerplaat(self) -> str:
        """Geeft het type van ankerplaat aan."""
        return self._typeAnkerplaat.get_waarde()

    @typeAnkerplaat.setter
    def typeAnkerplaat(self, value):
        self._typeAnkerplaat.set_waarde(value, owner=self)
