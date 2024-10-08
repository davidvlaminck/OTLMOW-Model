# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBGSchermelementtype(KeuzelijstField):
    """Het type bijzonder-schermelement."""
    naam = 'KlBGSchermelementtype'
    label = 'Bijzonder geluidsschermelementtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBGSchermelementtype'
    definition = 'Het type bijzonder-schermelement.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBGSchermelementtype'
    options = {
        'bloembakelement': KeuzelijstWaarde(invulwaarde='bloembakelement',
                                            label='bloembakelement',
                                            status='ingebruik',
                                            definitie='bloembakelement',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBGSchermelementtype/bloembakelement'),
        'l-element': KeuzelijstWaarde(invulwaarde='l-element',
                                      label='L-element',
                                      status='ingebruik',
                                      definitie='L-element',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBGSchermelementtype/l-element')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

