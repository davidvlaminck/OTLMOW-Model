# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPyranometerModelnaam(KeuzelijstField):
    """Pyranometer modelnamen."""
    naam = 'KlPyranometerModelnaam'
    label = 'Pyranometer modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPyranometerModelnaam'
    definition = 'Pyranometer modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPyranometerModelnaam'
    options = {
        'nr-lite2': KeuzelijstWaarde(invulwaarde='nr-lite2',
                                     label='NR Lite2',
                                     status='ingebruik',
                                     definitie='NR Lite2',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPyranometerModelnaam/nr-lite2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

