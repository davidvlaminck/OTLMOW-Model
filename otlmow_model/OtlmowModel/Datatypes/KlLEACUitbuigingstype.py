# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACUitbuigingstype(KeuzelijstField):
    """De mogelijke uitbuigingstypes."""
    naam = 'KlLEACUitbuigingstype'
    label = 'Uitbuigingstype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACUitbuigingstype'
    definition = 'De mogelijke uitbuigingstypes.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACUitbuigingstype'
    options = {
        'type-1': KeuzelijstWaarde(invulwaarde='type-1',
                                   label='type 1',
                                   status='ingebruik',
                                   definitie='Uitbuiging op wegen tot 90 km/h, straal R = 10 meter',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACUitbuigingstype/type-1'),
        'type-2': KeuzelijstWaarde(invulwaarde='type-2',
                                   label='type 2',
                                   status='ingebruik',
                                   definitie='Uitbuiging op wegen vanaf 90 km/h, L = 25 meter',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACUitbuigingstype/type-2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

