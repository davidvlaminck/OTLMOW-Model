# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLichtmastArmlengte(KeuzelijstField):
    """Lengte van de arm van de lichtmast in meter."""
    naam = 'KlWvLichtmastArmlengte'
    label = 'WV-mast armlengte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastArmlengte'
    definition = 'Lengte van de arm van de lichtmast in meter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLichtmastArmlengte'
    options = {
        '0-8': KeuzelijstWaarde(invulwaarde='0-8',
                                label='0.8',
                                status='ingebruik',
                                definitie='0.8',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/0-8'),
        '1.5': KeuzelijstWaarde(invulwaarde='1.5',
                                label='1.5',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/1.5'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/2'),
        '2.5': KeuzelijstWaarde(invulwaarde='2.5',
                                label='2.5',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/2.5'),
        '3.2': KeuzelijstWaarde(invulwaarde='3.2',
                                label='3.2',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/3.2'),
        'niet-van-toepassing': KeuzelijstWaarde(invulwaarde='niet-van-toepassing',
                                                label='niet van toepassing',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastArmlengte/niet-van-toepassing')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

