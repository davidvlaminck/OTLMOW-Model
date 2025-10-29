# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLuidsprekerModelnaam(KeuzelijstField):
    """De modelnaam van de luidspreker."""
    naam = 'KlLuidsprekerModelnaam'
    label = 'Luidspreker modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLuidsprekerModelnaam'
    definition = 'De modelnaam van de luidspreker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLuidsprekerModelnaam'
    options = {
        'abf-260-100w-pa6-v0': KeuzelijstWaarde(invulwaarde='abf-260-100w-pa6-v0',
                                                label='ABF-260/100W PA6 V0',
                                                status='ingebruik',
                                                definitie='ABF-260/100W PA6 V0',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuidsprekerModelnaam/abf-260-100w-pa6-v0')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

