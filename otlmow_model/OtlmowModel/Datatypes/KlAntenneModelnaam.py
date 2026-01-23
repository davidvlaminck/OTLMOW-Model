# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntenneModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Antenne."""
    naam = 'KlAntenneModelnaam'
    label = 'Antenne modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntenneModelnaam'
    definition = 'Keuzelijst met modelnamen voor Antenne.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntenneModelnaam'
    options = {
        'cm-s1-08nj': KeuzelijstWaarde(invulwaarde='cm-s1-08nj',
                                       label='CM-S1-08NJ',
                                       status='ingebruik',
                                       definitie='CM-S1-08NJ',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntenneModelnaam/cm-s1-08nj')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

