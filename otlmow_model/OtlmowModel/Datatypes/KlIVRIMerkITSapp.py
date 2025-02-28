# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIMerkITSapp(KeuzelijstField):
    """Het merk van de ITSapp."""
    naam = 'KlIVRIMerkITSapp'
    label = 'iVRIMerkITSapp'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIMerkITSapp'
    definition = 'Het merk van de ITSapp.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIMerkITSapp'
    options = {
        'goudappel': KeuzelijstWaarde(invulwaarde='goudappel',
                                      label='Goudappel',
                                      status='ingebruik',
                                      definitie='Goudappel',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkITSapp/goudappel'),
        'peek': KeuzelijstWaarde(invulwaarde='peek',
                                 label='Peek',
                                 status='ingebruik',
                                 definitie='Peek',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkITSapp/peek'),
        'rhdhv': KeuzelijstWaarde(invulwaarde='rhdhv',
                                  label='RHDHV',
                                  status='ingebruik',
                                  definitie='RHDHV',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIMerkITSapp/rhdhv')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

