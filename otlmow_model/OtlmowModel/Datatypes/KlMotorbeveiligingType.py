# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMotorbeveiligingType(KeuzelijstField):
    """Types voor toestellen voor motorbeveiliging volgens de toegepaste techniek."""
    naam = 'KlMotorbeveiligingType'
    label = 'Motorbeveiliging type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMotorbeveiligingType'
    definition = 'Types voor toestellen voor motorbeveiliging volgens de toegepaste techniek.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMotorbeveiligingType'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

