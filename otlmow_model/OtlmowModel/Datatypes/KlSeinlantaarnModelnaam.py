# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinlantaarnModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Seinlantaarn."""
    naam = 'KlSeinlantaarnModelnaam'
    label = 'seinlantaarn modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSeinlantaarnModelnaam'
    definition = 'Keuzelijst met modelnamen voor Seinlantaarn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinlantaarnModelnaam'
    options = {
        'alustar': KeuzelijstWaarde(invulwaarde='alustar',
                                    label='Alustar',
                                    status='ingebruik',
                                    definitie='Alustar',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnModelnaam/alustar'),
        'ciway': KeuzelijstWaarde(invulwaarde='ciway',
                                  label='CIWAY',
                                  status='ingebruik',
                                  definitie='CIWAY',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnModelnaam/ciway'),
        'futurit': KeuzelijstWaarde(invulwaarde='futurit',
                                    label='Futurit',
                                    status='ingebruik',
                                    definitie='Futurit',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnModelnaam/futurit')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

