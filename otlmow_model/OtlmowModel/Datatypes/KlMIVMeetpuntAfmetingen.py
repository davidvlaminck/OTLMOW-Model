# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVMeetpuntAfmetingen(KeuzelijstField):
    """Lijst van standaardafmetingen van een lus van een MIV meetpunt."""
    naam = 'KlMIVMeetpuntAfmetingen'
    label = 'MIV meetpunt afmetingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMIVMeetpuntAfmetingen'
    definition = 'Lijst van standaardafmetingen van een lus van een MIV meetpunt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVMeetpuntAfmetingen'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

