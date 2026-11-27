# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlMateriaalTaatsmechanisme import KlMateriaalTaatsmechanisme
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Taatspot(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een onderdeel van het taatsmechanisme dat bevestigd is aan het vast gedeelte van de bouwkundige constructie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspot'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ConstructieElementSluisStuw', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspen', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Taatsmechanisme', 'o', None),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._materiaalTaatspot = OTLAttribuut(field=KlMateriaalTaatsmechanisme,
                                               naam='materiaalTaatspot',
                                               label='materiaal taatspot',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Taatspot.materiaalTaatspot',
                                               definition='Het materiaal van de taatspot.',
                                               owner=self)

    @property
    def materiaalTaatspot(self) -> str:
        """Het materiaal van de taatspot."""
        return self._materiaalTaatspot.get_waarde()

    @materiaalTaatspot.setter
    def materiaalTaatspot(self, value):
        self._materiaalTaatspot.set_waarde(value, owner=self)
