# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElectricityAppurtenanceType(KeuzelijstField):
    """Lijst voor types van de ElectricityAppurtenance."""
    naam = 'KlElectricityAppurtenanceType'
    label = 'Electricity appurtenance type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlElectricityAppurtenanceType'
    definition = 'Lijst voor types van de ElectricityAppurtenance.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElectricityAppurtenanceType'
    options = {
        'aarding': KeuzelijstWaarde(invulwaarde='aarding',
                                    label='aarding',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricityAppurtenanceType/aarding'),
        'deliverypoint': KeuzelijstWaarde(invulwaarde='deliverypoint',
                                          label='deliveryPoint',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricityAppurtenanceType/deliverypoint'),
        'mof': KeuzelijstWaarde(invulwaarde='mof',
                                label='mof',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricityAppurtenanceType/mof'),
        'streetlight': KeuzelijstWaarde(invulwaarde='streetlight',
                                        label='streetLight',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricityAppurtenanceType/streetlight')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

