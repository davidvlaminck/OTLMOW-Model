# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeetcelNauwkeurigheidsvermogen(KeuzelijstField):
    """Nauwkeurigheidsvermogen van de meetcel in voltampère (bv. 5 of 15)."""
    naam = 'KlMeetcelNauwkeurigheidsvermogen'
    label = 'Meetcel nauwkeurigheidsvermogen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetcelNauwkeurigheidsvermogen'
    definition = 'Nauwkeurigheidsvermogen van de meetcel in voltampère (bv. 5 of 15).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetcelNauwkeurigheidsvermogen'
    options = {
        '15': KeuzelijstWaarde(invulwaarde='15',
                               label='15',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsvermogen/15'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsvermogen/5')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

