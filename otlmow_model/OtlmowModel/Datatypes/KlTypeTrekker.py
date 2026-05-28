# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeTrekker(KeuzelijstField):
    """Het type trekker."""
    naam = 'KlTypeTrekker'
    label = 'Type trekker'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeTrekker'
    definition = 'Het type trekker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeTrekker'
    options = {
        'kabel': KeuzelijstWaarde(invulwaarde='kabel',
                                  label='kabel',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeTrekker/kabel'),
        'staaf': KeuzelijstWaarde(invulwaarde='staaf',
                                  label='staaf',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeTrekker/staaf')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

