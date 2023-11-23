# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHydrantKoppeling(KeuzelijstField):
    """Keuzelijst met types koppelingen van hydranten."""
    naam = 'KlHydrantKoppeling'
    label = 'Hydrant koppeling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHydrantKoppeling'
    definition = 'Keuzelijst met types koppelingen van hydranten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHydrantKoppeling'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

