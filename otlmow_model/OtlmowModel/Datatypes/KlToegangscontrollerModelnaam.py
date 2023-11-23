# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangscontrollerModelnaam(KeuzelijstField):
    """Lijst met modelnamen voor toegangscontrollers volgens de fabrikant"""
    naam = 'KlToegangscontrollerModelnaam'
    label = 'Toegangscontroller modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToegangscontrollerModelnaam'
    definition = 'Lijst met modelnamen voor toegangscontrollers volgens de fabrikant'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangscontrollerModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

