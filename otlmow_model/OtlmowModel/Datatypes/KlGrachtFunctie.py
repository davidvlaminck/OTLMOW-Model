# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrachtFunctie(KeuzelijstField):
    """Mogelijke functies van de gracht."""
    naam = 'KlGrachtFunctie'
    label = 'Gracht functie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGrachtFunctie'
    definition = 'Mogelijke functies van de gracht.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrachtFunctie'
    options = {
        'baangracht': KeuzelijstWaarde(invulwaarde='baangracht',
                                       label='baangracht',
                                       status='ingebruik',
                                       definitie='Baangracht als functie van de gracht.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrachtFunctie/baangracht'),
        'ontwatering': KeuzelijstWaarde(invulwaarde='ontwatering',
                                        label='ontwatering',
                                        status='ingebruik',
                                        definitie='Ontwatering als functie van de gracht.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrachtFunctie/ontwatering'),
        'polder': KeuzelijstWaarde(invulwaarde='polder',
                                   label='polder',
                                   status='ingebruik',
                                   definitie='Polder als functie van de gracht.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrachtFunctie/polder'),
        'vesting': KeuzelijstWaarde(invulwaarde='vesting',
                                    label='vesting',
                                    status='ingebruik',
                                    definitie='Vesting als functie van de gracht.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrachtFunctie/vesting')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

