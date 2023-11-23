# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPompGroepModelnaam(KeuzelijstField):
    """De modelnaam van de pompgroep."""
    naam = 'KlPompGroepModelnaam'
    label = 'Pompgroep modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPompGroepModelnaam'
    definition = 'De modelnaam van de pompgroep.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPompGroepModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

