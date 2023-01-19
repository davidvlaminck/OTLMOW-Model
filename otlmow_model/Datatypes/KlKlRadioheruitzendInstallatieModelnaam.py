# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKlRadioheruitzendInstallatieModelnaam(KeuzelijstField):
    """De modelnamen voor een Radioheruitzendinstallatie."""
    naam = 'KlKlRadioheruitzendInstallatieModelnaam'
    label = 'Radioheruitzendinstallatie modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlKlRadioheruitzendInstallatieModelnaam'
    definition = 'De modelnamen voor een Radioheruitzendinstallatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKlRadioheruitzendInstallatieModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

