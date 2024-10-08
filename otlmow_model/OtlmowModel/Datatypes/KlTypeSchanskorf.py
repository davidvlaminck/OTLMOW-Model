# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeSchanskorf(KeuzelijstField):
    """Keuzelijst met de verschillende types schanskorven."""
    naam = 'KlTypeSchanskorf'
    label = 'Type schanskorf'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeSchanskorf'
    definition = 'Keuzelijst met de verschillende types schanskorven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeSchanskorf'
    options = {
        '4-5-x-4-5': KeuzelijstWaarde(invulwaarde='4-5-x-4-5',
                                      label='4.5 x 4.5',
                                      status='ingebruik',
                                      definitie='4.5 x 4.5',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSchanskorf/4-5-x-4-5'),
        '5-x-7': KeuzelijstWaarde(invulwaarde='5-x-7',
                                  label='5 x 7',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSchanskorf/5-x-7'),
        '6-x-8': KeuzelijstWaarde(invulwaarde='6-x-8',
                                  label='6 x 8',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeSchanskorf/6-x-8')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

