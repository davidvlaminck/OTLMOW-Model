# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class TijdelijkeOpslagplaats(AIMNaamObject, VlakGeometrie):
    """Permanent terrein voor tijdelijke opslag van materialen, grond, maaisel etc. gedurende de uitvoering van werken. Het opgeslagen materiaal wordt na de uitvoering van de werken van het terrein verwijderd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#TijdelijkeOpslagplaats'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Slagboom', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afsluiting', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangspoort', direction='i')  # i = direction: incoming
