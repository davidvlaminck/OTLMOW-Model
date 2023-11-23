# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitvoeringswijzeBoorpaal(KeuzelijstField):
    """De manier waarop de boorpaal is uitgevoerd."""
    naam = 'KlUitvoeringswijzeBoorpaal'
    label = 'Uitvoeringswijze boorpaal.'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUitvoeringswijzeBoorpaal'
    definition = 'De manier waarop de boorpaal is uitgevoerd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitvoeringswijzeBoorpaal'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

