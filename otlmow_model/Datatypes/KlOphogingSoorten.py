# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOphogingSoorten(KeuzelijstField):
    """De specificatie van type grond bij ophoging."""
    naam = 'KlOphogingSoorten'
    label = 'Ophoging soorten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlOphogingSoorten'
    definition = 'De specificatie van type grond bij ophoging.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOphogingSoorten'
    options = {
        'in-den-droge': KeuzelijstWaarde(invulwaarde='in-den-droge',
                                         label='in den droge',
                                         status='ingebruik',
                                         definitie='Grond met verwijdering naar een vergunde stortplaats.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOphogingSoorten/in-den-droge'),
        'onbevaarbare-waterlopen': KeuzelijstWaarde(invulwaarde='onbevaarbare-waterlopen',
                                                    label='onbevaarbare waterlopen',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOphogingSoorten/onbevaarbare-waterlopen'),
        'strandzand': KeuzelijstWaarde(invulwaarde='strandzand',
                                       label='strandzand',
                                       status='ingebruik',
                                       definitie='Grond met verwijdering naar een grondreinigingsbedrijf.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOphogingSoorten/strandzand'),
        'zeezand': KeuzelijstWaarde(invulwaarde='zeezand',
                                    label='zeezand',
                                    status='ingebruik',
                                    definitie='Grond met verwijdering naar een grondreinigingsbedrijf.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOphogingSoorten/zeezand')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

