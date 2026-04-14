# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftKeuring(DirectioneleRelatie):
    """Deze relatie legt een link tussen een object, onderdeel of installatie en een keuring (of keuringsdocument) dat op dat object van toepassing is. De richting loopt vanuit het fysieke object naar de bijhorende keuring."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftKeuring'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
