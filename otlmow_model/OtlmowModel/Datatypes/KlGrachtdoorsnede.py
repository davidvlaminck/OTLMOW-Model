# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrachtdoorsnede(KeuzelijstField):
    """De mogelijke doorsnedes van de gracht."""
    naam = 'KlGrachtdoorsnede'
    label = 'Grachtdoorsnede'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGrachtdoorsnede'
    definition = 'De mogelijke doorsnedes van de gracht.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrachtdoorsnede'
    options = {
        'groter-dan-1-5-m': KeuzelijstWaarde(invulwaarde='groter-dan-1-5-m',
                                             label='groter dan 1.5 m²',
                                             status='ingebruik',
                                             definitie='> 1.5 m²',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrachtdoorsnede/groter-dan-1-5-m'),
        'kleiner-of-gelijk-aan-1-5-m': KeuzelijstWaarde(invulwaarde='kleiner-of-gelijk-aan-1-5-m',
                                                        label='kleiner of gelijk aan 1.5 m²',
                                                        status='ingebruik',
                                                        definitie='<= 1.5 m²',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrachtdoorsnede/kleiner-of-gelijk-aan-1-5-m')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

