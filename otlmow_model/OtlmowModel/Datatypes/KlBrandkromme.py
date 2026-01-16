# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandkromme(KeuzelijstField):
    """Keuzelijst met de verschillende specifieke temperatuur-tijdscurves die als belasting is gehanteerd bij de validatie van de brandweerstand."""
    naam = 'KlBrandkromme'
    label = 'brandkromme'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandkromme'
    definition = 'Keuzelijst met de verschillende specifieke temperatuur-tijdscurves die als belasting is gehanteerd bij de validatie van de brandweerstand.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandkromme'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

