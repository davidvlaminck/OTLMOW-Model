# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCSchermtype(KeuzelijstField):
    """De mogelijke schermtypes (vlak, niet-vlak)."""
    naam = 'KlLEGCSchermtype'
    label = 'Schermtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCSchermtype'
    definition = 'De mogelijke schermtypes (vlak, niet-vlak).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCSchermtype'
    options = {
        'niet-vlak': KeuzelijstWaarde(invulwaarde='niet-vlak',
                                      label='niet-vlak',
                                      status='ingebruik',
                                      definitie='De niet-vlakke schermen zijn de schermen die niet kunnen getest worden volgens de normen NBN EN 1793-1 NBN EN 1793-2.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermtype/niet-vlak'),
        'vlak': KeuzelijstWaarde(invulwaarde='vlak',
                                 label='vlak',
                                 status='ingebruik',
                                 definitie='De vlakke schermen zijn de schermen die kunnen getest worden volgens de normen NBN EN 1793-1 NBN EN 1793-2.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCSchermtype/vlak')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

