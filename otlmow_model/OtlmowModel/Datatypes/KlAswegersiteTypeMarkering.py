# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAswegersiteTypeMarkering(KeuzelijstField):
    """Lijst met mogelijke types van markeringen bij een aswegersite."""
    naam = 'KlAswegersiteTypeMarkering'
    label = 'Type markering aswegersite'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAswegersiteTypeMarkering'
    definition = 'Lijst met mogelijke types van markeringen bij een aswegersite.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAswegersiteTypeMarkering'
    options = {
        'stopstreep': KeuzelijstWaarde(invulwaarde='stopstreep',
                                       label='Stopstreep',
                                       status='ingebruik',
                                       definitie='Stopstreep',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAswegersiteTypeMarkering/stopstreep'),
        'stopstreep-en-pijl': KeuzelijstWaarde(invulwaarde='stopstreep-en-pijl',
                                               label='Stopstreep en pijl',
                                               status='ingebruik',
                                               definitie='Stopstreep en pijl',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAswegersiteTypeMarkering/stopstreep-en-pijl')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

