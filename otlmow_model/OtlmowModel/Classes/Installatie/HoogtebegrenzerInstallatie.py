# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HoogtebegrenzerInstallatie(AIMNaamObject, LijnGeometrie):
    """Een mechanische en/of elektronische opstelling die bij kunstwerken (zoals bruggen of tunnels) de maximale doorrijhoogte van voertuigen detecteert en overtredingen voorkomt om schade te vermijden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#HoogtebegrenzerInstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtebegrenzer', direction='i')  # i = direction: incoming
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#RetroreflecterendVerkeersbord', direction='i')  # i = direction: incoming
