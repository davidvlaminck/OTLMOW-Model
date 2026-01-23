# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPLCMerk(KeuzelijstField):
    """Het merk van de PLC."""
    naam = 'KlPLCMerk'
    label = 'PLC merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPLCMerk'
    definition = 'Het merk van de PLC.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPLCMerk'
    options = {
        'philips': KeuzelijstWaarde(invulwaarde='philips',
                                    label='Philips',
                                    status='ingebruik',
                                    definitie='Philips',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCMerk/philips'),
        'phoenix-contact': KeuzelijstWaarde(invulwaarde='phoenix-contact',
                                            label='Phoenix Contact',
                                            status='ingebruik',
                                            definitie='Phoenix Contact',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCMerk/phoenix-contact'),
        'siemens': KeuzelijstWaarde(invulwaarde='siemens',
                                    label='Siemens',
                                    status='ingebruik',
                                    definitie='Siemens',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCMerk/siemens'),
        'vaisala': KeuzelijstWaarde(invulwaarde='vaisala',
                                    label='Vaisala',
                                    status='ingebruik',
                                    definitie='Vaisala',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCMerk/vaisala')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

