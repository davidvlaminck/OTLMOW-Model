# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRadioheruitzendInstallatieMerk(KeuzelijstField):
    """De mogelijke merken van een radioheruitzendinstallatie."""
    naam = 'KlRadioheruitzendInstallatieMerk'
    label = 'Radioheruitzendinstallatie merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlRadioheruitzendInstallatieMerk'
    definition = 'De mogelijke merken van een radioheruitzendinstallatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRadioheruitzendInstallatieMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

