# coding=utf-8
from otlmow_model.Classes.Abstracten.BevestigingGC import BevestigingGC
from otlmow_model.Classes.Abstracten.Deur import Deur
from otlmow_model.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vluchtdeur(BevestigingGC, Deur, AIMNaamObject):
    """Deur voor het ontvluchten in geval van calamiteiten weg van de incidentlocatie naar een veilige zone. Een vluchtdeur wordt onder alle omstandigheden zonder sleutel geopend en dit met beperkte kracht."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vluchtdeur'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aanstraalverlichting')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contourverlichting')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie')
