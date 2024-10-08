# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVWCTypeNivelleringssysteem(KeuzelijstField):
    """De mogelijke typen van het nivelleringssysteem van een vaste waterbouwkundige constructie."""
    naam = 'KlVWCTypeNivelleringssysteem'
    label = 'Type nivelleringssysteem'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlVWCTypeNivelleringssysteem'
    definition = 'De mogelijke typen van het nivelleringssysteem van een vaste waterbouwkundige constructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVWCTypeNivelleringssysteem'
    options = {
        'door-de-deur': KeuzelijstWaarde(invulwaarde='door-de-deur',
                                         label='door de deur',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVWCTypeNivelleringssysteem/door-de-deur'),
        'niet-van-toepassing': KeuzelijstWaarde(invulwaarde='niet-van-toepassing',
                                                label='niet van toepassing',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVWCTypeNivelleringssysteem/niet-van-toepassing'),
        'omloopriolen': KeuzelijstWaarde(invulwaarde='omloopriolen',
                                         label='omloopriolen',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVWCTypeNivelleringssysteem/omloopriolen'),
        'onder-de-deur': KeuzelijstWaarde(invulwaarde='onder-de-deur',
                                          label='onder de deur',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVWCTypeNivelleringssysteem/onder-de-deur')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

