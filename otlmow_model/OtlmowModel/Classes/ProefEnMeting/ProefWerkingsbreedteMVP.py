# coding=utf-8
from ...Classes.Abstracten.Proef import Proef
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWerkingsbreedteMVP(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """Proef om de afstand tussen de voorkant van het onvervormd systeem tot de maximale dynamische laterale positie van elk onderdeel van het systeem te bepalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWerkingsbreedteMVP'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Motorvangplank', direction='o', deprecated='2.0.0')  # o = direction: outgoing
