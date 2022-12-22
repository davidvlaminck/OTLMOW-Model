# coding=utf-8
from otlmow_model.Classes.Abstracten.AanhorighedenBrug import AanhorighedenBrug
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VoorzieningNegatieveReactie(AanhorighedenBrug, AIMNaamObject, VlakGeometrie):
    """Voorziening om opwaartse reacties ter hoogte van de steunpunten tegen te gaan, bv. stalen staven. Dit element maakt de verbinding tussen brugdeel en landhoofd/pijler en bevindt zich in de onmiddellijke omgeving van de opleggingen. De oplegging (dit is een andere klasse) kan zowel druk als trek opnemen en kan ook gebruikt worden als een voorziening tegen negatieve reactie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VoorzieningNegatieveReactie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        AanhorighedenBrug.__init__(self)
        VlakGeometrie.__init__(self)
