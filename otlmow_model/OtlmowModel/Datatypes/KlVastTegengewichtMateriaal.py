# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVastTegengewichtMateriaal(KeuzelijstField):
    """De mogelijke materialen van een vast tegengewicht."""
    naam = 'KlVastTegengewichtMateriaal'
    label = 'Vast tegengewicht materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlVastTegengewichtMateriaal'
    definition = 'De mogelijke materialen van een vast tegengewicht.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVastTegengewichtMateriaal'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVastTegengewichtMateriaal/andere'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVastTegengewichtMateriaal/beton'),
        'beton-met-toevoeging-van-staal': KeuzelijstWaarde(invulwaarde='beton-met-toevoeging-van-staal',
                                                           label='beton met toevoeging van staal',
                                                           status='ingebruik',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVastTegengewichtMateriaal/beton-met-toevoeging-van-staal'),
        'lood': KeuzelijstWaarde(invulwaarde='lood',
                                 label='lood',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVastTegengewichtMateriaal/lood'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVastTegengewichtMateriaal/staal'),
        'vloeistof': KeuzelijstWaarde(invulwaarde='vloeistof',
                                      label='vloeistof',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVastTegengewichtMateriaal/vloeistof'),
        'zwaar-beton': KeuzelijstWaarde(invulwaarde='zwaar-beton',
                                        label='zwaar beton',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVastTegengewichtMateriaal/zwaar-beton')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

