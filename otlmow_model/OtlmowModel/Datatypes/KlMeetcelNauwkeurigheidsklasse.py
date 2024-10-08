# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeetcelNauwkeurigheidsklasse(KeuzelijstField):
    """Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...)."""
    naam = 'KlMeetcelNauwkeurigheidsklasse'
    label = 'Meetcel nauwkeurigheidsklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetcelNauwkeurigheidsklasse'
    definition = 'Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetcelNauwkeurigheidsklasse'
    options = {
        '0.2': KeuzelijstWaarde(invulwaarde='0.2',
                                label='0.2',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsklasse/0.2'),
        '0.2-S': KeuzelijstWaarde(invulwaarde='0.2-S',
                                  label='0.2 S',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsklasse/0.2-S'),
        '0.5': KeuzelijstWaarde(invulwaarde='0.5',
                                label='0.5',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsklasse/0.5')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

