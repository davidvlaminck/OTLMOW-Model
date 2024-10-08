# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBewerkingsmanierMetselwerk(KeuzelijstField):
    """De manier waarop het metselwerk bewerkt wordt."""
    naam = 'KlBewerkingsmanierMetselwerk'
    label = 'Bewerkingsmanier metselwerk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBewerkingsmanierMetselwerk'
    definition = 'De manier waarop het metselwerk bewerkt wordt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBewerkingsmanierMetselwerk'
    options = {
        'bezet': KeuzelijstWaarde(invulwaarde='bezet',
                                  label='Bezet',
                                  status='ingebruik',
                                  definitie='Het metselwerk werd bezet.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewerkingsmanierMetselwerk/bezet'),
        'gelaagd': KeuzelijstWaarde(invulwaarde='gelaagd',
                                    label='Gelaagd',
                                    status='ingebruik',
                                    definitie='Bij gelaagd metselwerk wordt gebruik gemaakt van gevlakte en gekanthouwde breuksteen.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewerkingsmanierMetselwerk/gelaagd'),
        'in-bossage-behouwen': KeuzelijstWaarde(invulwaarde='in-bossage-behouwen',
                                                label='In bossage behouwen',
                                                status='ingebruik',
                                                definitie='Een bewerking in reliÃ«f, waarbij de voorkant ruw gehakt wordt.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewerkingsmanierMetselwerk/in-bossage-behouwen'),
        'niet-bezet': KeuzelijstWaarde(invulwaarde='niet-bezet',
                                       label='Niet bezet',
                                       status='ingebruik',
                                       definitie='Het metselwerk werd niet bezet.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewerkingsmanierMetselwerk/niet-bezet'),
        'niet-gelaagd': KeuzelijstWaarde(invulwaarde='niet-gelaagd',
                                         label='Niet gelaagd',
                                         status='ingebruik',
                                         definitie='Bij niet gelaagd metselwerk wordt gebruik gemaakt van niet-gevlakte en niet-gekanthouwde breuksteen.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBewerkingsmanierMetselwerk/niet-gelaagd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

