# coding=utf-8
from ...Classes.ImplementatieElement.AIMObject import AIMObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynamischeVluchtwegindicatie(AIMObject, PuntGeometrie):
    """Armaturen die ingezet worden indien er alternatieve vluchtconcepten worden toegepast. De vluchtroute loopt dan meestal gedeeltelijk door de ondersteunende koker. De borden geven de te volgen vluchtroute aan en zijn pas zichtbaar zodra ze worden ingeschakeld. Bij evacuatie kan er ook een extra ondersteunende omroepbericht worden ingezet."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynamischeVluchtwegindicatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Vluchtganginrichting', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart', direction='u')  # u = unidirectional
