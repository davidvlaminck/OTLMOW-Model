# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KLLuidsprekerVormgeving(KeuzelijstField):
    """Types luidspreker volgens hun vormfactor."""
    naam = 'KLLuidsprekerVormgeving'
    label = 'Luidspreker vormgeving'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KLLuidsprekerVormgeving'
    definition = 'Types luidspreker volgens hun vormfactor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KLLuidsprekerVormgeving'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

