# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeVakwerkElement(KeuzelijstField):
    """Het type van vakwerk-element."""
    naam = 'KlTypeVakwerkElement'
    label = 'Type vakwerk-element'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeVakwerkElement'
    definition = 'Het type van vakwerk-element.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeVakwerkElement'
    options = {
        'bovenregel': KeuzelijstWaarde(invulwaarde='bovenregel',
                                       label='Bovenregel',
                                       status='ingebruik',
                                       definitie='Bovenregel bij vakwerk.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVakwerkElement/bovenregel'),
        'diagonaal': KeuzelijstWaarde(invulwaarde='diagonaal',
                                      label='Diagonaal',
                                      status='ingebruik',
                                      definitie='Diagonale staaf bij vakwerk.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVakwerkElement/diagonaal'),
        'onderregel': KeuzelijstWaarde(invulwaarde='onderregel',
                                       label='Onderregel',
                                       status='ingebruik',
                                       definitie='Onderregel bij vakwerk.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVakwerkElement/onderregel'),
        'stijl': KeuzelijstWaarde(invulwaarde='stijl',
                                  label='Stijl',
                                  status='ingebruik',
                                  definitie='Verticale staaf bij vakwerk.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVakwerkElement/stijl')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

