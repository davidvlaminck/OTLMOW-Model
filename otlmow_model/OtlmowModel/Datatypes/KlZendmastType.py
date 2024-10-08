# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZendmastType(KeuzelijstField):
    """Keuzelijst voor de types zendmast."""
    naam = 'KlZendmastType'
    label = 'Zendmast type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZendmastType'
    definition = 'Keuzelijst voor de types zendmast.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZendmastType'
    options = {
        'conische-mast': KeuzelijstWaarde(invulwaarde='conische-mast',
                                          label='conische mast',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZendmastType/conische-mast'),
        'vakwerkmast': KeuzelijstWaarde(invulwaarde='vakwerkmast',
                                        label='vakwerkmast',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZendmastType/vakwerkmast')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

