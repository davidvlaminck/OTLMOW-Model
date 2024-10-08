# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEnergiemeterMetertype(KeuzelijstField):
    """Type meter (mechanisch, elektronisch)."""
    naam = 'KlEnergiemeterMetertype'
    label = 'Elektrisch metertype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlEnergiemeterMetertype'
    definition = 'Type meter (mechanisch, elektronisch).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEnergiemeterMetertype'
    options = {
        'elektronisch': KeuzelijstWaarde(invulwaarde='elektronisch',
                                         label='elektronisch',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterMetertype/elektronisch'),
        'mechanisch': KeuzelijstWaarde(invulwaarde='mechanisch',
                                       label='mechanisch',
                                       status='ingebruik',
                                       definitie='Nakijken bij EVT',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterMetertype/mechanisch')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

