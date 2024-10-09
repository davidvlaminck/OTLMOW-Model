# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BasisverlichtingTunnel(AIMNaamObject, VlakGeometrie):
    """Het geheel van verlichtingstoestellen dat over de hele lengte van de koker loopt en met verschillende regimes het verlichtingsniveau voor de koker kan bepalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BasisverlichtingTunnel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Tunnelverlichting', direction='o')  # o = direction: outgoing
