# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtzuilSoortLamp(KeuzelijstField):
    """Soort lamp voor de lichtzuilen."""
    naam = 'KlLichtzuilSoortLamp'
    label = 'Lichtzuil soort lamp'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtzuilSoortLamp'
    definition = 'Soort lamp voor de lichtzuilen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtzuilSoortLamp'
    options = {
        'gloeilamp': KeuzelijstWaarde(invulwaarde='gloeilamp',
                                      label='gloeilamp',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtzuilSoortLamp/gloeilamp'),
        'halogeen': KeuzelijstWaarde(invulwaarde='halogeen',
                                     label='halogeen',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtzuilSoortLamp/halogeen'),
        'led': KeuzelijstWaarde(invulwaarde='led',
                                label='LED',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtzuilSoortLamp/led'),
        'spaarlamp': KeuzelijstWaarde(invulwaarde='spaarlamp',
                                      label='spaarlamp',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtzuilSoortLamp/spaarlamp'),
        'tl': KeuzelijstWaarde(invulwaarde='tl',
                               label='TL',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtzuilSoortLamp/tl')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

