# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKokerTypeFundering(KeuzelijstField):
    """Keuzelijst om aan te geven welk type fundering gebruikt is in de kokercel."""
    naam = 'KlKokerTypeFundering'
    label = 'Koker type fundering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlKokerTypeFundering'
    definition = 'Keuzelijst om aan te geven welk type fundering gebruikt is in de kokercel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKokerTypeFundering'
    options = {
        'niet-gekend': KeuzelijstWaarde(invulwaarde='niet-gekend',
                                        label='niet gekend',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKokerTypeFundering/niet-gekend'),
        'niet-opgenomen-in-de-lijst': KeuzelijstWaarde(invulwaarde='niet-opgenomen-in-de-lijst',
                                                       label='niet opgenomen in de lijst',
                                                       status='ingebruik',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKokerTypeFundering/niet-opgenomen-in-de-lijst'),
        'op-palen': KeuzelijstWaarde(invulwaarde='op-palen',
                                     label='op palen',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKokerTypeFundering/op-palen'),
        'op-staal': KeuzelijstWaarde(invulwaarde='op-staal',
                                     label='op staal',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKokerTypeFundering/op-staal'),
        'putfundering': KeuzelijstWaarde(invulwaarde='putfundering',
                                         label='putfundering',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKokerTypeFundering/putfundering')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

