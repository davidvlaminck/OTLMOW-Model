# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftBijlage(DirectioneleRelatie):
    """Deze relatie legt een link tussen een object/onderdeel/installatie en een (bestands)bijlage. De richting loopt vanuit het fysiek object naar de bijlage."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBijlage'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
