# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeGrendel(KeuzelijstField):
    """Lijst van mogelijke types grendels."""
    naam = 'KlTypeGrendel'
    label = 'Type grendel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeGrendel'
    definition = 'Lijst van mogelijke types grendels.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeGrendel'
    options = {
        'klauw': KeuzelijstWaarde(invulwaarde='klauw',
                                  label='klauw',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeGrendel/klauw'),
        'pen': KeuzelijstWaarde(invulwaarde='pen',
                                label='pen',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeGrendel/pen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

