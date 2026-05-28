# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeHoogtebegrenzer(KeuzelijstField):
    """De mogelijke types van een hoogtebegrenzer."""
    naam = 'KlTypeHoogtebegrenzer'
    label = 'type hoogtebegrenzer'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeHoogtebegrenzer'
    definition = 'De mogelijke types van een hoogtebegrenzer.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeHoogtebegrenzer'
    options = {
        'balk': KeuzelijstWaarde(invulwaarde='balk',
                                 label='balk',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeHoogtebegrenzer/balk'),
        'ketting': KeuzelijstWaarde(invulwaarde='ketting',
                                    label='ketting',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeHoogtebegrenzer/ketting'),
        'koker': KeuzelijstWaarde(invulwaarde='koker',
                                  label='koker',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeHoogtebegrenzer/koker')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

