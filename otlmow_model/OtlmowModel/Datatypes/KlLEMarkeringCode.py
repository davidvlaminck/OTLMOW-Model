# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEMarkeringCode(KeuzelijstField):
    """Codes van de markering op lijnvormige elementen."""
    naam = 'KlLEMarkeringCode'
    label = 'Markering code'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEMarkeringCode'
    definition = 'Codes van de markering op lijnvormige elementen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEMarkeringCode'
    options = {
        'DIV-BIG': KeuzelijstWaarde(invulwaarde='DIV-BIG',
                                    label='DIV-BIG',
                                    status='ingebruik',
                                    definitie='De code voor LE markering biggenrug',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-BIG'),
        'DIV-BRDSTN': KeuzelijstWaarde(invulwaarde='DIV-BRDSTN',
                                       label='DIV-BRDSTN',
                                       status='ingebruik',
                                       definitie='De code voor LE markering boordsteen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-BRDSTN'),
        'DIV-BRDSTN-PV': KeuzelijstWaarde(invulwaarde='DIV-BRDSTN-PV',
                                          label='DIV-BRDSTN-PV',
                                          status='ingebruik',
                                          definitie='De code voor LE markering boordsteen parkeerverbod',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-BRDSTN-PV'),
        'DIV-NJ': KeuzelijstWaarde(invulwaarde='DIV-NJ',
                                   label='DIV-NJ',
                                   status='ingebruik',
                                   definitie='De code voor LE markering New Jersey',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringCode/DIV-NJ')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

