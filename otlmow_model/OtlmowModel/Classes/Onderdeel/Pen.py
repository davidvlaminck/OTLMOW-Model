# coding=utf-8
from ...Classes.Abstracten.Aangrijping import Aangrijping
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pen(Aangrijping, AIMNaamObject):
    """Een verbindingsonderdeel die zorgt voor de koppeling tussen de beweegbare constructie en de vaste constructie. Dit kan ook als aangrijpingspunt dienen in het geval van uitkragende pennen, bijvoorbeeld bij beweegbare bruggen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aangrijpingsstoel', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#CilinderStangkop', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Halsbeugelmechanisme', direction='o')  # o = direction: outgoing
