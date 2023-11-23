# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDieptetemperatuursensorModelnaam(KeuzelijstField):
    """Dieptetemperatuursensor modelnamen."""
    naam = 'KlDieptetemperatuursensorModelnaam'
    label = 'Dieptetemperatuursensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDieptetemperatuursensorModelnaam'
    definition = 'Dieptetemperatuursensor modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDieptetemperatuursensorModelnaam'
    options = {
        'dts12g': KeuzelijstWaarde(invulwaarde='dts12g',
                                   label='DTS12G',
                                   status='ingebruik',
                                   definitie='DTS12G',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDieptetemperatuursensorModelnaam/dts12g')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

