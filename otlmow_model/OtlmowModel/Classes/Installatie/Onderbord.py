# coding=utf-8
from ...Classes.Onderdeel.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderbord(RetroreflecterendVerkeersbord, PuntGeometrie):
    """Een bord met een verkeersteken dat als toevoeging onder een verkeersbord is gehangen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Onderbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
