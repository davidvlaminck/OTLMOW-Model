# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalDraineerlaag(KeuzelijstField):
    """De mogelijke materialen waaruit een draineerlaag is opgebouwd."""
    naam = 'KlMateriaalDraineerlaag'
    label = 'Materiaal draineerlaag'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalDraineerlaag'
    definition = 'De mogelijke materialen waaruit een draineerlaag is opgebouwd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalDraineerlaag'
    options = {
        'breuksteen': KeuzelijstWaarde(invulwaarde='breuksteen',
                                       label='breuksteen',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDraineerlaag/breuksteen'),
        'grind': KeuzelijstWaarde(invulwaarde='grind',
                                  label='grind',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDraineerlaag/grind'),
        'zand': KeuzelijstWaarde(invulwaarde='zand',
                                 label='zand',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDraineerlaag/zand')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

