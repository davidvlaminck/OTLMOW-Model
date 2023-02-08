# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeHorizontalePlaat(KeuzelijstField):
    """Het type horizontale plaat."""
    naam = 'KlTypeHorizontalePlaat'
    label = 'Type horizontale plaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeHorizontalePlaat'
    definition = 'Het type horizontale plaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeHorizontalePlaat'
    options = {
        'dakplaat': KeuzelijstWaarde(invulwaarde='dakplaat',
                                     label='Dakplaat',
                                     status='ingebruik',
                                     definitie='Plaat die het dak van een constructie vormt.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeHorizontalePlaat/dakplaat'),
        'onderplaat': KeuzelijstWaarde(invulwaarde='onderplaat',
                                       label='Onderplaat',
                                       status='ingebruik',
                                       definitie='Plaat die de bodem/vloer vormt van een constructie. Ook bodemplaat of vloerplaat genoemd.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeHorizontalePlaat/onderplaat'),
        'tussenplaat': KeuzelijstWaarde(invulwaarde='tussenplaat',
                                        label='Tussenplaat',
                                        status='ingebruik',
                                        definitie='Plaat tussen twee kunstwerken, bv. kokers.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeHorizontalePlaat/tussenplaat')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

