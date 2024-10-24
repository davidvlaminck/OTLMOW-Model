# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeGrondanker(KeuzelijstField):
    """De mogelijke types grondanker."""
    naam = 'KlTypeGrondanker'
    label = 'Type grondanker'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTypeGrondanker'
    definition = 'De mogelijke types grondanker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeGrondanker'
    options = {
        'duo': KeuzelijstWaarde(invulwaarde='duo',
                                label='duo',
                                status='ingebruik',
                                definitie='duo',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeGrondanker/duo'),
        'gestaffeld': KeuzelijstWaarde(invulwaarde='gestaffeld',
                                       label='gestaffeld',
                                       status='ingebruik',
                                       definitie='gestaffeld',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeGrondanker/gestaffeld'),
        'mono': KeuzelijstWaarde(invulwaarde='mono',
                                 label='mono',
                                 status='ingebruik',
                                 definitie='mono',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeGrondanker/mono')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

