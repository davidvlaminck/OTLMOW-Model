# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOntvangerToepassing(KeuzelijstField):
    """Keuzelijst met modelnamen voor OntvangerToepassing."""
    naam = 'KlOntvangerToepassing'
    label = 'Ontvanger toepassing'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOntvangerToepassing'
    definition = 'Keuzelijst met modelnamen voor OntvangerToepassing.'
    status = 'ingebruik'
    deprecated_version = '2.8.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOntvangerToepassing'
    options = {
        'GPRS': KeuzelijstWaarde(invulwaarde='GPRS',
                                 label='GPRS',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/GPRS'),
        'GSM': KeuzelijstWaarde(invulwaarde='GSM',
                                label='GSM',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/GSM'),
        'KAR': KeuzelijstWaarde(invulwaarde='KAR',
                                label='KAR',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/KAR'),
        'WIFI': KeuzelijstWaarde(invulwaarde='WIFI',
                                 label='WIFI',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOntvangerToepassing/WIFI')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

