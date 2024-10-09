# coding=utf-8
from ...Classes.Abstracten.AanhorighedenBrug import AanhorighedenBrug
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VoorzieningNegatieveReactie(AanhorighedenBrug, AIMNaamObject, LijnGeometrie):
    """Voorziening om opwaartse reacties ter hoogte van de steunpunten tegen te gaan, bv. stalen staven. Dit element maakt de verbinding tussen brugdeel en landhoofd/pijler en bevindt zich in de onmiddellijke omgeving van de opleggingen. De oplegging (dit is een andere klasse) kan zowel druk als trek opnemen en kan ook gebruikt worden als een voorziening tegen negatieve reactie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VoorzieningNegatieveReactie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Oplegrij', direction='o')  # o = direction: outgoing
