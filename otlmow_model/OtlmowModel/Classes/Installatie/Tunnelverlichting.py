# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Tunnelverlichting(AIMNaamObject, VlakGeometrie):
    """Het systeem van verlichtingselementen en armaturen, typisch ontworpen en geïnstalleerd in een tunnel, om aangepaste lichtniveaus volgens verschillende regimes te bieden voor veilig verkeer en zichtbaarheid binnenin een koker."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Tunnelverlichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BasisverlichtingTunnel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VersterkingsverlichtingTunnel', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtsensor', direction='i')  # i = direction: incoming
