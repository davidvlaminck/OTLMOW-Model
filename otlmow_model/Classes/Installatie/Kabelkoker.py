# coding=utf-8
from otlmow_model.Classes.Abstracten.Kabelgeleiding import Kabelgeleiding
from otlmow_model.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelkoker(Kabelgeleiding, LijnGeometrie):
    """Een ruimte die een of meerdere kabels of leidingen beschermt tegen beschadiging en/of de kabels of leidingen op een gecontroleerde plaats laat hangen of liggen. De constructieve elementen die de ruimte creëeren vormen een aaneen- en afgesloten geheel dat niet meer uit elkaar kan gehaald worden. De kabels en leidingen zijn enkel nog toegankelijk door in de koker zelf rond te lopen (of te kruipen). De koker is op die toegankelijkheid voorzien."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kabelkoker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderdoorboring')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwaterkruising')
