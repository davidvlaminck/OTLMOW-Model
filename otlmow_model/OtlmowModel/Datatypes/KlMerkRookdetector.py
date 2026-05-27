# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMerkRookdetector(KeuzelijstField):
    """Het merk van de rookdetector."""
    naam = 'KlMerkRookdetector'
    label = 'merk rookdetector'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMerkRookdetector'
    definition = 'Het merk van de rookdetector.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMerkRookdetector'
    options = {
        'kidde': KeuzelijstWaarde(invulwaarde='kidde',
                                  label='Kidde',
                                  status='ingebruik',
                                  definitie='Kidde',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMerkRookdetector/kidde')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

