# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeVoeg(KeuzelijstField):
    """Het type van de metselvoeg."""
    naam = 'KlTypeVoeg'
    label = 'Type metselvoeg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeVoeg'
    definition = 'Het type van de metselvoeg.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeVoeg'
    options = {
        'dunmortel': KeuzelijstWaarde(invulwaarde='dunmortel',
                                      label='dunmortel',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVoeg/dunmortel'),
        'klassiek': KeuzelijstWaarde(invulwaarde='klassiek',
                                     label='klassiek',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVoeg/klassiek'),
        'verlijmd': KeuzelijstWaarde(invulwaarde='verlijmd',
                                     label='verlijmd',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVoeg/verlijmd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

