# coding=utf-8
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vluchtdeurindicatie(AIMObject, VlakGeometrie):
    """De componenten die visuele of audiovisuele aanwijzingen bieden over de plaats in een koker waar een vluchtdeur of vluchtopening te vinden is, zodat mensen snel en effectief kunnen worden geleid naar veilige uitgangen tijdens een noodsituatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtdeurindicatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
