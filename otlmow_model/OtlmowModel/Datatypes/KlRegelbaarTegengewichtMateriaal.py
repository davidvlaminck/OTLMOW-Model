# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRegelbaarTegengewichtMateriaal(KeuzelijstField):
    """De mogelijke materialen als regelbaar tegengewicht."""
    naam = 'KlRegelbaarTegengewichtMateriaal'
    label = 'Regelbaar tegengewicht materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlRegelbaarTegengewichtMateriaal'
    definition = 'De mogelijke materialen als regelbaar tegengewicht.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRegelbaarTegengewichtMateriaal'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelbaarTegengewichtMateriaal/andere'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelbaarTegengewichtMateriaal/beton'),
        'gietijzer': KeuzelijstWaarde(invulwaarde='gietijzer',
                                      label='gietijzer',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelbaarTegengewichtMateriaal/gietijzer'),
        'lood': KeuzelijstWaarde(invulwaarde='lood',
                                 label='lood',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelbaarTegengewichtMateriaal/lood'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelbaarTegengewichtMateriaal/staal'),
        'vloeistof': KeuzelijstWaarde(invulwaarde='vloeistof',
                                      label='vloeistof',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRegelbaarTegengewichtMateriaal/vloeistof')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

