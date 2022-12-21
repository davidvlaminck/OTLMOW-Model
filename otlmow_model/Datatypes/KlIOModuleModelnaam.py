# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOModuleModelnaam(KeuzelijstField):
    """Lijst van modelnamen van I/O-modules volgens de fabrikant."""
    naam = 'KlIOModuleModelnaam'
    label = 'Modelnaam I/O-module'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOModuleModelnaam'
    definition = 'Lijst van modelnamen van I/O-modules volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOModuleModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

