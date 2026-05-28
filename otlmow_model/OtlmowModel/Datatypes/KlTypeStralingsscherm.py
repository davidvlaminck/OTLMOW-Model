# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeStralingsscherm(KeuzelijstField):
    """Types van stralingsschermen."""
    naam = 'KlTypeStralingsscherm'
    label = 'Type stralingsscherm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeStralingsscherm'
    definition = 'Types van stralingsschermen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeStralingsscherm'
    options = {
        'beschermingshut': KeuzelijstWaarde(invulwaarde='beschermingshut',
                                            label='beschermingshut',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeStralingsscherm/beschermingshut'),
        'beschermingskap': KeuzelijstWaarde(invulwaarde='beschermingskap',
                                            label='beschermingskap',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeStralingsscherm/beschermingskap'),
        'geen': KeuzelijstWaarde(invulwaarde='geen',
                                 label='geen',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeStralingsscherm/geen'),
        'vaisala-dtr13': KeuzelijstWaarde(invulwaarde='vaisala-dtr13',
                                          label='Vaisala DTR13',
                                          status='uitgebruik',
                                          definitie='Vaisala DTR13',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeStralingsscherm/vaisala-dtr13')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

