# coding=utf-8
from ...Classes.Abstracten.StaalsoortObject import StaalsoortObject
from ...Classes.Abstracten.TechnischDocument import TechnischDocument
from ...Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from otlmow_model.OtlmowModel.GeometrieTypes.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Halsbeugelpen(StaalsoortObject, TechnischDocument, AIMNaamObject, PuntGeometrie):
    """Een onderdeel van het halsbeugelmechanisme dat is geïntegreerd in de sluisdeur. Deze pen fungeert als draaipunt voor de bewegingen van de deur. Rondom de pen zijn het lagerelement en het halsbeugeloog geplaatst, die de beweging ondersteunen en eventueel reguleren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Halsbeugelpen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Halsbeugelmechanisme', direction='o')  # o = direction: outgoing
