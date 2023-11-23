# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeegsensorModelnaam(KeuzelijstField):
    """De modelnaam van de weegsensor."""
    naam = 'KlWeegsensorModelnaam'
    label = 'Weegsensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegsensorModelnaam'
    definition = 'De modelnaam van de weegsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegsensorModelnaam'
    options = {
        'lineas-wim-sensor-9195gc41': KeuzelijstWaarde(invulwaarde='lineas-wim-sensor-9195gc41',
                                                       label='Lineas WIM Sensor 9195GC41',
                                                       status='ingebruik',
                                                       definitie='Lineas WIM Sensor 9195GC41',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegsensorModelnaam/lineas-wim-sensor-9195gc41'),
        'lineas-wim-sensor-9195gc51': KeuzelijstWaarde(invulwaarde='lineas-wim-sensor-9195gc51',
                                                       label='Lineas WIM Sensor 9195GC51',
                                                       status='ingebruik',
                                                       definitie='Lineas WIM Sensor 9195GC51',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegsensorModelnaam/lineas-wim-sensor-9195gc51')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

