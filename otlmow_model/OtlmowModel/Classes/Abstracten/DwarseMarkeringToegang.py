# coding=utf-8
from abc import abstractmethod
from ...Classes.Abstracten.AOWSType import AOWSType
from ...Classes.Abstracten.Markering import Markering
from otlmow_model.OtlmowModel.GeometrieTypes.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class DwarseMarkeringToegang(AOWSType, Markering, VlakGeometrie):
    """Abstracte als toegang tot de verschillende soorten dwarse markeringen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DwarseMarkeringToegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepDwarseMarkeringEnFiguratie', direction='o')  # o = direction: outgoing
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GroepMarkering', direction='o')  # o = direction: outgoing
