# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACSchokindexMVP(KeuzelijstField):
    """Head injury criteria (HIC) van een motorvangplank."""
    naam = 'KlLEACSchokindexMVP'
    label = 'Schokindex MVP'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACSchokindexMVP'
    definition = 'Head injury criteria (HIC) van een motorvangplank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACSchokindexMVP'
    options = {
        'level-1': KeuzelijstWaarde(invulwaarde='level-1',
                                    label='level 1',
                                    status='ingebruik',
                                    definitie='Krachten op hoofd en nek worden beperkt tijdens test',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSchokindexMVP/level-1'),
        'level-2': KeuzelijstWaarde(invulwaarde='level-2',
                                    label='level 2',
                                    status='ingebruik',
                                    definitie='Krachten op hoofd en nek worden tot levensgevaarlijk tijdens test',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACSchokindexMVP/level-2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

