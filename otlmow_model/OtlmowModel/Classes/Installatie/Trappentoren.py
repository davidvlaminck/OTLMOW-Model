# coding=utf-8
from ...Classes.Abstracten.AanhorigheidKoker import AanhorigheidKoker
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Trappentoren(AanhorigheidKoker, AIMNaamObject, VlakGeometrie):
    """Een trappentoren is een geïntegreerde constructie van trappen die kan dienen om 1 of meerdere niveaus te beklimmen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Trappentoren'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.12.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kokerruimte', direction='u', deprecated='2.12.0')  # u = unidirectional
