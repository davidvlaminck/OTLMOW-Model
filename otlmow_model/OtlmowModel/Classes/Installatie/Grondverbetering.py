# coding=utf-8
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Grondverbetering(AIMNaamObject, VlakGeometrie):
    """Proces waarbij de fysieke eigenschappen van de grond worden aangepast om de draagkracht te verhogen, de samendrukbaarheid te verminderen, en de stabiliteit te verbeteren, door technieken zoals verdichting, chemische stabilisatie, het gebruik van geokunststoffen, en het aanbrengen van grindkernen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Grondverbetering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Grindkern', direction='i')  # i = direction: incoming
