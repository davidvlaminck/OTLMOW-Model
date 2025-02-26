# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRadarModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Radar."""
    naam = 'KlRadarModelnaam'
    label = 'Radar modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRadarModelnaam'
    definition = 'Keuzelijst met modelnamen voor Radar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRadarModelnaam'
    options = {
        'tma-011': KeuzelijstWaarde(invulwaarde='tma-011',
                                    label='TMA-011',
                                    status='ingebruik',
                                    definitie='TMA-011',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRadarModelnaam/tma-011'),
        'tma-122': KeuzelijstWaarde(invulwaarde='tma-122',
                                    label='TMA-122',
                                    status='ingebruik',
                                    definitie='TMA-122',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRadarModelnaam/tma-122'),
        'tma-296': KeuzelijstWaarde(invulwaarde='tma-296',
                                    label='TMA-296',
                                    status='ingebruik',
                                    definitie='TMA-296',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRadarModelnaam/tma-296'),
        'tma-60': KeuzelijstWaarde(invulwaarde='tma-60',
                                   label='TMA-60',
                                   status='ingebruik',
                                   definitie='TMA-60',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRadarModelnaam/tma-60'),
        'tmb-134': KeuzelijstWaarde(invulwaarde='tmb-134',
                                    label='TMB-134',
                                    status='ingebruik',
                                    definitie='TMB-134',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRadarModelnaam/tmb-134')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

