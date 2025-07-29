# coding=utf-8
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Houdriem(TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een flexibel of stijf mechanisch element dat wordt toegepast in balgmechanismen. Het dient om te zorgen dat de beweging van de balg gecontroleerd of gelimiteerd wordt en binnen veilige grenzen blijft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Houdriem'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bufferinstallatie', direction='o')  # o = direction: outgoing
