# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomStandplaatswaarde(KeuzelijstField):
    """De verschillende opties van de standplaatswaarde voor een boom."""
    naam = 'KlBoomStandplaatswaarde'
    label = 'Boom standplaatswaarde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomStandplaatswaarde'
    definition = 'De verschillende opties van de standplaatswaarde voor een boom.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomStandplaatswaarde'
    options = {
        '0.6': KeuzelijstWaarde(invulwaarde='0.6',
                                label='0.6',
                                status='ingebruik',
                                definitie='Landelijk gebied',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.6'),
        '0.7': KeuzelijstWaarde(invulwaarde='0.7',
                                label='0.7',
                                status='ingebruik',
                                definitie='Overgangszone: bebouwde kom - landelijk gebied',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.7'),
        '0.8': KeuzelijstWaarde(invulwaarde='0.8',
                                label='0.8',
                                status='ingebruik',
                                definitie='Open en halfopen bebouwing',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.8'),
        '0.9': KeuzelijstWaarde(invulwaarde='0.9',
                                label='0.9',
                                status='ingebruik',
                                definitie='Gesloten bebouwing',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/0.9'),
        '06': KeuzelijstWaarde(invulwaarde='06',
                               label='0.6',
                               status='ingebruik',
                               definitie='0.6',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/06'),
        '07': KeuzelijstWaarde(invulwaarde='07',
                               label='0.7',
                               status='ingebruik',
                               definitie='0.7',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/07'),
        '08': KeuzelijstWaarde(invulwaarde='08',
                               label='0.8',
                               status='ingebruik',
                               definitie='0.8',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/08'),
        '09': KeuzelijstWaarde(invulwaarde='09',
                               label='0.9',
                               status='ingebruik',
                               definitie='0.9',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/09'),
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie='1',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/1'),
        '1.0': KeuzelijstWaarde(invulwaarde='1.0',
                                label='1.0',
                                status='ingebruik',
                                definitie='Sterk verstedelijkte stads- of dorpskern',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomStandplaatswaarde/1.0')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

