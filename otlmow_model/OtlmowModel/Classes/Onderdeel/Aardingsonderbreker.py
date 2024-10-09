# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aardingsonderbreker(AIMNaamObject, PuntGeometrie):
    """De verbindingsklem waarop de aardgeleider(s), de hoofdbeschermingsgeleider(s), en de hoofdequipotentiaalgeleider(s) toekomen. Het gaat om een T-vormige klem, waarbij de functie van meetklem en hoofdaardingsklem wordt gecombineerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingsonderbreker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie', direction='o')  # o = direction: outgoing
