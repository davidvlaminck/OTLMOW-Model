# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeIVSB(KeuzelijstField):
    """De mogelijke types van een inwendig verlicht signalisatiebord."""
    naam = 'KlTypeIVSB'
    label = 'type inwendig verlicht signalisatiebord'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeIVSB'
    definition = 'De mogelijke types van een inwendig verlicht signalisatiebord.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeIVSB'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='Andere',
                                   status='ingebruik',
                                   definitie='Andere',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeIVSB/andere'),
        'refractoren': KeuzelijstWaarde(invulwaarde='refractoren',
                                        label='Refractoren',
                                        status='ingebruik',
                                        definitie='Refractoren',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeIVSB/refractoren'),
        'tl-lampen': KeuzelijstWaarde(invulwaarde='tl-lampen',
                                      label='TL lampen',
                                      status='ingebruik',
                                      definitie='TL lampen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeIVSB/tl-lampen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

