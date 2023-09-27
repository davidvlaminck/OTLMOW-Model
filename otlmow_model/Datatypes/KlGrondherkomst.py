# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrondherkomst(KeuzelijstField):
    """De herkomst van de grond."""
    naam = 'KlGrondherkomst'
    label = 'Grondherkomst'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlGrondherkomst'
    definition = 'De herkomst van de grond.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrondherkomst'
    options = {
        'aanbestedende-overheid': KeuzelijstWaarde(invulwaarde='aanbestedende-overheid',
                                                   label='aanbestedende overheid',
                                                   status='ingebruik',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondherkomst/aanbestedende-overheid'),
        'ander-project': KeuzelijstWaarde(invulwaarde='ander-project',
                                          label='ander project',
                                          status='ingebruik',
                                          definitie='Grond voor tijdelijke opslag binnen de werfzone.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondherkomst/ander-project'),
        'de-aannemer': KeuzelijstWaarde(invulwaarde='de-aannemer',
                                        label='de aannemer',
                                        status='ingebruik',
                                        definitie='Grond met verwijdering naar een grondreinigingsbedrijf.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondherkomst/de-aannemer'),
        'gezeefde-gronden': KeuzelijstWaarde(invulwaarde='gezeefde-gronden',
                                             label='gezeefde gronden',
                                             status='ingebruik',
                                             definitie='Grond met verwijdering naar een vergunde stortplaats.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondherkomst/gezeefde-gronden'),
        'werfzone': KeuzelijstWaarde(invulwaarde='werfzone',
                                     label='werfzone',
                                     status='ingebruik',
                                     definitie='Grond voor hergebruik binnen de werfzone.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrondherkomst/werfzone')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

