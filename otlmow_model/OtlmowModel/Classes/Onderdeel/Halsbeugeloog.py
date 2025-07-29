# coding=utf-8
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Halsbeugeloog(StaalsoortObject, TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een oogvormig onderdeel, geïntegreerd in een halsbeugelmechanisme, dat dient als bevestigingspunt van de halsbeugelpen met het gedeelte dat op beton is gemonteerd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Halsbeugeloog'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Lager', direction='u')  # u = unidirectional
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Halsbeugelmechanisme', direction='o')  # o = direction: outgoing
