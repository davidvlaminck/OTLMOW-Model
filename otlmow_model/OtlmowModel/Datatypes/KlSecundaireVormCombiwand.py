# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSecundaireVormCombiwand(KeuzelijstField):
    """De mogelijke secundaire vormen van een combiwand."""
    naam = 'KlSecundaireVormCombiwand'
    label = 'Secundaire combiwand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlSecundaireVormCombiwand'
    definition = 'De mogelijke secundaire vormen van een combiwand.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSecundaireVormCombiwand'
    options = {
        'platte-damplank': KeuzelijstWaarde(invulwaarde='platte-damplank',
                                            label='Platte damplank',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSecundaireVormCombiwand/platte-damplank'),
        'u-vorm': KeuzelijstWaarde(invulwaarde='u-vorm',
                                   label='U-vorm',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSecundaireVormCombiwand/u-vorm'),
        'z-vorm': KeuzelijstWaarde(invulwaarde='z-vorm',
                                   label='Z-vorm',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSecundaireVormCombiwand/z-vorm')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

