# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalStraatkap(KeuzelijstField):
    """Het materiaal van een straatkap verwijst naar de specifieke bouwstof of samenstelling waaruit het deksel bestaat."""
    naam = 'KlMateriaalStraatkap'
    label = 'Keuzelijst materiaal straatkap'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalStraatkap'
    definition = 'Het materiaal van een straatkap verwijst naar de specifieke bouwstof of samenstelling waaruit het deksel bestaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalStraatkap'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

