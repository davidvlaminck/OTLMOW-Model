# coding=utf-8
from otlmow_model.Classes.Abstracten.AndereLaag import AndereLaag
from otlmow_model.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GeexpandeerdPolystyreen(AndereLaag, VlakGeometrie):
    """Geëxpandeerd polystyreen of PS-hardschuim is een karakteristieke en vrijwel altijd witte kunststof, in de volksmond piepschuim genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeexpandeerdPolystyreen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')
