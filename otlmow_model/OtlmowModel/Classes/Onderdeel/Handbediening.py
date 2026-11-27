# coding=utf-8
from typing import ClassVar

from ...BaseClasses.OTLObject import OTLAttribuut
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...Datatypes.KlHandbedieningType import KlHandbedieningType
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Handbediening(AIMNaamObject, PuntGeometrie):
    """Module voor het bedienen met de hand van een techniek die zich in de kast bevindt waaraan de module bevestigd is om de sturing van de betrokken techniek tijdelijk over te nemen of uit te lezen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handbediening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegkantkast', 'u', None),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LEDBord', 'u', None),  # u = unidirectional
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)

        self._type = OTLAttribuut(field=KlHandbedieningType,
                                  naam='type',
                                  label='type handbediening',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handbediening.type',
                                  definition='Het gebruikte type voor handbediening langs de buitenkant van een kast voor sturing van systemen binnenin.',
                                  owner=self)

    def _get_type(self) -> str:
        """Het gebruikte type voor handbediening langs de buitenkant van een kast voor sturing van systemen binnenin."""
        return self._type.get_waarde()

    def _set_type(self, value):
        self._type.set_waarde(value, owner=self)
    type = property(_get_type, _set_type)
