# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBrugdekvoeg(KeuzelijstField):
    """Het type van de brugdekvoeg."""
    naam = 'KlTypeBrugdekvoeg'
    label = 'Type brugdekvoeg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBrugdekvoeg'
    definition = 'Het type van de brugdekvoeg.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBrugdekvoeg'
    options = {
        'compound-voeg': KeuzelijstWaarde(invulwaarde='compound-voeg',
                                          label='Compound voeg',
                                          status='ingebruik',
                                          definitie='(Flexibele) voegovergang op basis van bitumen (compoundvoeg).',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdekvoeg/compound-voeg'),
        'getande-voeg-met-voegband': KeuzelijstWaarde(invulwaarde='getande-voeg-met-voegband',
                                                      label='Getande voeg met voegband',
                                                      status='ingebruik',
                                                      definitie='Brugdekvoeg van het type klauwprofiel, met voegband.',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdekvoeg/getande-voeg-met-voegband'),
        'getande-voeg-zonder-voegband': KeuzelijstWaarde(invulwaarde='getande-voeg-zonder-voegband',
                                                         label='Getande voeg zonder voegband',
                                                         status='ingebruik',
                                                         definitie='Brugdekvoeg van het type klauwprofiel, zonder voegband.',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdekvoeg/getande-voeg-zonder-voegband'),
        'niet-gekend': KeuzelijstWaarde(invulwaarde='niet-gekend',
                                        label='Niet gekend',
                                        status='ingebruik',
                                        definitie='Het type brugdekvoeg is niet gekend.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdekvoeg/niet-gekend'),
        'polymeer-voeg': KeuzelijstWaarde(invulwaarde='polymeer-voeg',
                                          label='Polymeer voeg',
                                          status='ingebruik',
                                          definitie='(Flexibele) voegovergang op basis van polymeren.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugdekvoeg/polymeer-voeg')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

