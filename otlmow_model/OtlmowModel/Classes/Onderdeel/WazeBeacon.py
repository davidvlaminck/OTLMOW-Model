# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class WazeBeacon(NaampadObject, PuntGeometrie):
    """Een Waze Beacon is een klein apparaat dat GPS-signalen versterkt in omgevingen zoals tunnels of ondergrondse parkeergarages, waar GPS-ontvangst zwak is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WazeBeacon'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand', direction='u')  # u = unidirectional
