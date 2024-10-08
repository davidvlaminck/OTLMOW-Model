# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVGSchermelementtype(KeuzelijstField):
    """Het type vlak-schermelement."""
    naam = 'KlVGSchermelementtype'
    label = 'Vlak geluidsschermelementtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVGSchermelementtype'
    definition = 'Het type vlak-schermelement.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVGSchermelementtype'
    options = {
        'schermelement-bevestigd-tegen-de-profielen': KeuzelijstWaarde(invulwaarde='schermelement-bevestigd-tegen-de-profielen',
                                                                       label='schermelement bevestigd tegen de profielen',
                                                                       status='ingebruik',
                                                                       definitie='schermelement bevestigd tegen de profielen',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGSchermelementtype/schermelement-bevestigd-tegen-de-profielen'),
        'schermelement-geplaatst-tussen-profielen': KeuzelijstWaarde(invulwaarde='schermelement-geplaatst-tussen-profielen',
                                                                     label='schermelement geplaatst tussen profielen',
                                                                     status='ingebruik',
                                                                     definitie='schermelement geplaatst tussen profielen',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGSchermelementtype/schermelement-geplaatst-tussen-profielen'),
        'schermelement-zonder-profielen': KeuzelijstWaarde(invulwaarde='schermelement-zonder-profielen',
                                                           label='schermelement zonder profielen',
                                                           status='ingebruik',
                                                           definitie='schermelement zonder profielen',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGSchermelementtype/schermelement-zonder-profielen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

