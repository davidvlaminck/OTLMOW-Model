# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDisplayType(KeuzelijstField):
    """Keuzelijst voor de verschillende technologieën voor displays."""
    naam = 'KlDisplayType'
    label = 'Display type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDisplayType'
    definition = 'Keuzelijst voor de verschillende technologieën voor displays.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDisplayType'
    options = {
        'lcd': KeuzelijstWaarde(invulwaarde='lcd',
                                label='LCD',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDisplayType/lcd'),
        'qled': KeuzelijstWaarde(invulwaarde='qled',
                                 label='QLED',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDisplayType/qled')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

