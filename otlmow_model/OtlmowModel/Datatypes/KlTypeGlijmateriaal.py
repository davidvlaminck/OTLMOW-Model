# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeGlijmateriaal(KeuzelijstField):
    """Lijst van mogelijke types glijmateriaal."""
    naam = 'KlTypeGlijmateriaal'
    label = 'Type glijmateriaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeGlijmateriaal'
    definition = 'Lijst van mogelijke types glijmateriaal.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeGlijmateriaal'
    options = {
        'glijblok': KeuzelijstWaarde(invulwaarde='glijblok',
                                     label='glijblok',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeGlijmateriaal/glijblok'),
        'glijstrip': KeuzelijstWaarde(invulwaarde='glijstrip',
                                      label='glijstrip',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeGlijmateriaal/glijstrip')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

