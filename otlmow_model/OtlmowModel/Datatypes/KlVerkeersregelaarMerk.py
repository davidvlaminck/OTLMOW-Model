# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Verkeersregelaar."""
    naam = 'KlVerkeersregelaarMerk'
    label = 'verkeersregelaar merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarMerk'
    definition = 'Keuzelijst met merknamen voor Verkeersregelaar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarMerk'
    options = {
        'dynniq': KeuzelijstWaarde(invulwaarde='dynniq',
                                   label='Dynniq',
                                   status='ingebruik',
                                   definitie='Dynniq',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/dynniq'),
        'ko-hartog': KeuzelijstWaarde(invulwaarde='ko-hartog',
                                      label='Ko Hartog',
                                      status='ingebruik',
                                      definitie='Ko Hartog',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/ko-hartog'),
        'peek': KeuzelijstWaarde(invulwaarde='peek',
                                 label='Peek',
                                 status='ingebruik',
                                 definitie='Peek',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/peek'),
        'siemens': KeuzelijstWaarde(invulwaarde='siemens',
                                    label='Siemens',
                                    status='ingebruik',
                                    definitie='Siemens',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/siemens'),
        'swarco': KeuzelijstWaarde(invulwaarde='swarco',
                                   label='Swarco',
                                   status='ingebruik',
                                   definitie='Swarco (voorheen Dynniq)',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/swarco'),
        'yunex': KeuzelijstWaarde(invulwaarde='yunex',
                                  label='Yunex',
                                  status='ingebruik',
                                  definitie='Yunex',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarMerk/yunex')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

