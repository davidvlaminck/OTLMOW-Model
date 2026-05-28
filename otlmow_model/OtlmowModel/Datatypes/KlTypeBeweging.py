# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBeweging(KeuzelijstField):
    """Mogelijk types van beweging"""
    naam = 'KlTypeBeweging'
    label = 'Type beweging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBeweging'
    definition = 'Mogelijk types van beweging'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBeweging'
    options = {
        'rotatie-rond-1-as': KeuzelijstWaarde(invulwaarde='rotatie-rond-1-as',
                                              label='rotatie rond 1 as',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweging/rotatie-rond-1-as'),
        'rotatie-rond-meerdere-assen': KeuzelijstWaarde(invulwaarde='rotatie-rond-meerdere-assen',
                                                        label='rotatie rond meerdere assen',
                                                        status='ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweging/rotatie-rond-meerdere-assen'),
        'translatie': KeuzelijstWaarde(invulwaarde='translatie',
                                       label='translatie',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeweging/translatie')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

