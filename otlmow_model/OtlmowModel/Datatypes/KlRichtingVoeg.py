# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRichtingVoeg(KeuzelijstField):
    """De richting van de voeg waarop de voegafdichting wordt geplaatst."""
    naam = 'KlRichtingVoeg'
    label = 'richting voeg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRichtingVoeg'
    definition = 'De richting van de voeg waarop de voegafdichting wordt geplaatst.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRichtingVoeg'
    options = {
        'dwars': KeuzelijstWaarde(invulwaarde='dwars',
                                  label='dwars',
                                  status='ingebruik',
                                  definitie='dwars',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRichtingVoeg/dwars'),
        'langs': KeuzelijstWaarde(invulwaarde='langs',
                                  label='langs',
                                  status='ingebruik',
                                  definitie='langs',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRichtingVoeg/langs')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

