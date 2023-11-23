# coding=utf-8
from ...Classes.Abstracten.VegetatieElement import VegetatieElement
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Muurvegetatie(VegetatieElement, PuntGeometrie):
    """Muurvegetaties zijn gebonden aan door de mens gecreëerde stenige, doorgaans steile tot verticale standplaatsen. Voorbeelden zijn kerkhofmuren, stadswallen, ruïnes, kademuren, oude forten en bunkers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurvegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
