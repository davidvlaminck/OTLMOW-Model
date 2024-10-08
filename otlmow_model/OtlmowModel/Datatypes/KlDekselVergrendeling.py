# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDekselVergrendeling(KeuzelijstField):
    """Manieren waarop het deksel is vergrendeld."""
    naam = 'KlDekselVergrendeling'
    label = 'Dekselvergrendeling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDekselVergrendeling'
    definition = 'Manieren waarop het deksel is vergrendeld.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDekselVergrendeling'
    options = {
        'bouten': KeuzelijstWaarde(invulwaarde='bouten',
                                   label='bouten',
                                   status='ingebruik',
                                   definitie='Het deksel is vergrendeld met inox schroefbouten met zeskantmoer',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselVergrendeling/bouten'),
        'haken': KeuzelijstWaarde(invulwaarde='haken',
                                  label='haken',
                                  status='ingebruik',
                                  definitie='Het deksel is met haken vergrendeld',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselVergrendeling/haken'),
        'inbus': KeuzelijstWaarde(invulwaarde='inbus',
                                  label='inbus',
                                  status='ingebruik',
                                  definitie='Het deksel is vergrendeld met inox schroefbouten met inbusmoer',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDekselVergrendeling/inbus')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

