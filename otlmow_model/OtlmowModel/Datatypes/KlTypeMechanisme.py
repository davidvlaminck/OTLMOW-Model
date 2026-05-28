# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeMechanisme(KeuzelijstField):
    """Lijst met de verschillende types mechanismen."""
    naam = 'KlTypeMechanisme'
    label = 'Type mechanisme'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeMechanisme'
    definition = 'Lijst met de verschillende types mechanismen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeMechanisme'
    options = {
        'los': KeuzelijstWaarde(invulwaarde='los',
                                label='los',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeMechanisme/los'),
        'vast': KeuzelijstWaarde(invulwaarde='vast',
                                 label='vast',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeMechanisme/vast')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

