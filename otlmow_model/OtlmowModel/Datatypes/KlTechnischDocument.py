# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTechnischDocument(KeuzelijstField):
    """Keuzelijst met de verschillende optie voor technische documenten"""
    naam = 'KlTechnischDocument'
    label = 'Keuzelijst technisch document'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTechnischDocument'
    definition = 'Keuzelijst met de verschillende optie voor technische documenten'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTechnischDocument'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

