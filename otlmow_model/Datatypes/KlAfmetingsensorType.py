# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfmetingsensorType(KeuzelijstField):
    """Het type van de afmetingsensor."""
    naam = 'KlAfmetingsensorType'
    label = 'Afmetingsensor type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfmetingsensorType'
    definition = 'Het type van de afmetingsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfmetingsensorType'
    options = {
        '2D-LIDAR': KeuzelijstWaarde(invulwaarde='2D-LIDAR',
                                     label='2D-LIDAR',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorType/2D-LIDAR'),
        'lussen-en-laserogen': KeuzelijstWaarde(invulwaarde='lussen-en-laserogen',
                                                label='lussen en laserogen',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorType/lussen-en-laserogen'),
        'radar': KeuzelijstWaarde(invulwaarde='radar',
                                  label='radar',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorType/radar')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

