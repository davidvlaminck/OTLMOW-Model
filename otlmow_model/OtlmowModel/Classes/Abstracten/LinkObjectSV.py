# coding=utf-8
from abc import abstractmethod
from ...Classes.Abstracten.BaseAttributenSV import BaseAttributenSV
from otlmow_model.OtlmowModel.BaseClasses.OTLAsset import OTLAsset
from otlmow_model.OtlmowModel.BaseClasses.RelationInteractor import RelationInteractor


# Generated with OTLClassCreator. To modify: extend, do not edit
class LinkObjectSV(BaseAttributenSV, RelationInteractor, OTLAsset):
    """Abstracte om relaties te linken op hoog niveau."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LinkObjectSV'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftBetrokkene', target='http://purl.org/dc/terms/Agent', direction='o')  # o = direction: outgoing
