# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlaatsingswijze(KeuzelijstField):
    """Mogelijke manieren van plaatsing van het straatmeubilair."""
    naam = 'KlPlaatsingswijze'
    label = 'Plaatsingswijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlaatsingswijze'
    definition = 'Mogelijke manieren van plaatsing van het straatmeubilair.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlaatsingswijze'
    options = {
        'vast': KeuzelijstWaarde(invulwaarde='vast',
                                 label='vast',
                                 status='ingebruik',
                                 definitie='Vaste plaatsing van het straatmeubilair.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijze/vast'),
        'wegneembaar': KeuzelijstWaarde(invulwaarde='wegneembaar',
                                        label='wegneembaar',
                                        status='ingebruik',
                                        definitie='Wegneembare plaatsing van het straatmeubilair.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlaatsingswijze/wegneembaar')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

