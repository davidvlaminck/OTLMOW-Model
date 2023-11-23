# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kokerventilatie(AIMNaamObject, VlakGeometrie):
    """Het geheel van ventilatoren, luchtkanalen, sensoren en regelapparatuur om de luchtsnelheid, luchtdruk en luchtsamenstelling in een koker te bewaken en aan te passen aan veranderende omstandigheden, zoals verkeerscongestie of noodsituaties zoals brand."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kokerventilatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
