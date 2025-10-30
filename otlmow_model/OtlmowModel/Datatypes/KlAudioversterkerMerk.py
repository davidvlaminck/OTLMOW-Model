# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAudioversterkerMerk(KeuzelijstField):
    """Het merk van de audioversterker."""
    naam = 'KlAudioversterkerMerk'
    label = 'Audioversterker merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAudioversterkerMerk'
    definition = 'Het merk van de audioversterker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAudioversterkerMerk'
    options = {
        'harman': KeuzelijstWaarde(invulwaarde='harman',
                                   label='Harman',
                                   status='ingebruik',
                                   definitie='Harman',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAudioversterkerMerk/harman')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

