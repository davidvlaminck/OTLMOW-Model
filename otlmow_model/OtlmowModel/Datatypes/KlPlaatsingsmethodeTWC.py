# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlaatsingsmethodeTWC(KeuzelijstField):
    """De mogelijke manieren of methodes om een tijdelijke waterkerende constrcutie te plaatsen."""
    naam = 'KlPlaatsingsmethodeTWC'
    label = 'Plaatsingsmethode TWC'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPlaatsingsmethodeTWC'
    definition = 'De mogelijke manieren of methodes om een tijdelijke waterkerende constrcutie te plaatsen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlaatsingsmethodeTWC'
    options = {
        'invaren': KeuzelijstWaarde(invulwaarde='invaren',
                                    label='invaren',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingsmethodeTWC/invaren'),
        'plaatsen-met-kraan': KeuzelijstWaarde(invulwaarde='plaatsen-met-kraan',
                                               label='plaatsen met kraan',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingsmethodeTWC/plaatsen-met-kraan')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

