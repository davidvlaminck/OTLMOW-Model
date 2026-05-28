# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBadge(KeuzelijstField):
    """De verschillende badgetypes."""
    naam = 'KlTypeBadge'
    label = 'Type badge'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTypeBadge'
    definition = 'De verschillende badgetypes.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBadge'
    options = {
        'facilitair-bedrijf': KeuzelijstWaarde(invulwaarde='facilitair-bedrijf',
                                               label='Facilitair bedrijf',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBadge/facilitair-bedrijf')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

