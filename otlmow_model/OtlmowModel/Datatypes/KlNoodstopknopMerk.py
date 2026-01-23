# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNoodstopknopMerk(KeuzelijstField):
    """Het merk van een noodstopknop."""
    naam = 'KlNoodstopknopMerk'
    label = 'Noodstopknop merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNoodstopknopMerk'
    definition = 'Het merk van een noodstopknop.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNoodstopknopMerk'
    options = {
        'abb': KeuzelijstWaarde(invulwaarde='abb',
                                label='ABB',
                                status='ingebruik',
                                definitie='ABB',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopMerk/abb'),
        'legrand': KeuzelijstWaarde(invulwaarde='legrand',
                                    label='Legrand',
                                    status='ingebruik',
                                    definitie='Legrand',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopMerk/legrand'),
        'pilz': KeuzelijstWaarde(invulwaarde='pilz',
                                 label='Pilz',
                                 status='ingebruik',
                                 definitie='Pilz',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopMerk/pilz'),
        'schneider': KeuzelijstWaarde(invulwaarde='schneider',
                                      label='Schneider',
                                      status='ingebruik',
                                      definitie='Schneider',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopMerk/schneider'),
        'wei': KeuzelijstWaarde(invulwaarde='wei',
                                label='WEI',
                                status='ingebruik',
                                definitie='WEI',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopMerk/wei')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

