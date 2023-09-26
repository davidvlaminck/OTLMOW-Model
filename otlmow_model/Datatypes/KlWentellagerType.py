# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWentellagerType(KeuzelijstField):
    """Keuzelijst voor de verschillende soorten wentellager."""
    naam = 'KlWentellagerType'
    label = 'Wentellager type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWentellagerType'
    definition = 'Keuzelijst voor de verschillende soorten wentellager.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWentellagerType'
    options = {
        'bollager': KeuzelijstWaarde(invulwaarde='bollager',
                                     label='bollager',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWentellagerType/bollager'),
        'cilinderlager': KeuzelijstWaarde(invulwaarde='cilinderlager',
                                          label='cilinderlager',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWentellagerType/cilinderlager'),
        'diabololager': KeuzelijstWaarde(invulwaarde='diabololager',
                                         label='diabololager',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWentellagerType/diabololager'),
        'kegellager': KeuzelijstWaarde(invulwaarde='kegellager',
                                       label='kegellager',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWentellagerType/kegellager'),
        'kogellager': KeuzelijstWaarde(invulwaarde='kogellager',
                                       label='kogellager',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWentellagerType/kogellager'),
        'naaldlager': KeuzelijstWaarde(invulwaarde='naaldlager',
                                       label='naaldlager',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWentellagerType/naaldlager'),
        'tonlager': KeuzelijstWaarde(invulwaarde='tonlager',
                                     label='tonlager',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWentellagerType/tonlager')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

