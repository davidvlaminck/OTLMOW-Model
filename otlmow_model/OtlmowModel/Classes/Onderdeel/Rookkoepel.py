# coding=utf-8
from ...Classes.ImplementatieElement.NaampadObject import NaampadObject
from ...GeometrieTypes.PuntGeometrie import PuntGeometrie
from ...GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rookkoepel(NaampadObject, PuntGeometrie, VlakGeometrie):
    """Een veiligheidssysteem dat bij brand automatisch opent om rook en warmte af te voeren, zodat het kokerdeel stroomopwaarts van de brand rookvrij blijft en de vluchtroutes toegankelijk blijven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rookkoepel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
