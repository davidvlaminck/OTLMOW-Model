# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aardingsrooster(AIMNaamObject, PuntGeometrie):
    """Een raster dat wordt gebruikt voor de aarding van elektrische installaties. Het biedt een veilige afvoer van elektrische stroom naar de aarde, waardoor de kans op elektrische schokken en schade aan apparatuur wordt verminderd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingsrooster'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie', direction='o')  # o = direction: outgoing
