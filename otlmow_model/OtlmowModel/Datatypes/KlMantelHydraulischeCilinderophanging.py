# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMantelHydraulischeCilinderophanging(KeuzelijstField):
    """De wijze van ophanging van de mantel van een hydraulische cilinder."""
    naam = 'KlMantelHydraulischeCilinderophanging'
    label = 'Mantel hydraulische Cinlinderophanging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMantelHydraulischeCilinderophanging'
    definition = 'De wijze van ophanging van de mantel van een hydraulische cilinder.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMantelHydraulischeCilinderophanging'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

