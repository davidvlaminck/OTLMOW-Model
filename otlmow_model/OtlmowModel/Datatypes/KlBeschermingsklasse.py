# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeschermingsklasse(KeuzelijstField):
    """Type van corrosiebescherming."""
    naam = 'KlBeschermingsklasse'
    label = 'beschermingsklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermingsklasse'
    definition = 'Type van corrosiebescherming.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermingsklasse'
    options = {
        'p1': KeuzelijstWaarde(invulwaarde='p1',
                               label='P1',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingsklasse/p1'),
        'p2': KeuzelijstWaarde(invulwaarde='p2',
                               label='P2',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingsklasse/p2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

