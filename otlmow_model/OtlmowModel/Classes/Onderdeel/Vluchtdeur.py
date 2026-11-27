# coding=utf-8
from typing import ClassVar

from ...Classes.Abstracten.BevestigingGC import BevestigingGC
from ...Classes.Abstracten.Deur import Deur
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vluchtdeur(BevestigingGC, Deur, AIMNaamObject):
    """Deur voor het ontvluchten in geval van calamiteiten weg van de incidentlocatie naar een veilige zone. Een vluchtdeur wordt onder alle omstandigheden zonder sleutel geopend en dit met beperkte kracht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vluchtdeur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.9.0'

    _VALID_RELATIONS: ClassVar[list[tuple[str, str, str, str | None]]] = [
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel', 'u', '2.9.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aanstraalverlichting', 'u', '2.9.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contourverlichting', 'u', '2.9.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram', 'u', '2.9.0'),  # u = unidirectional
        ('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie', 'o', '2.9.0'),  # o = direction: outgoing
    ]

    def __init__(self):
        super().__init__()

        self.add_valid_relations(self._VALID_RELATIONS)
