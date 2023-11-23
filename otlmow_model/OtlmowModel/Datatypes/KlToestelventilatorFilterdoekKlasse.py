# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToestelventilatorFilterdoekKlasse(KeuzelijstField):
    """Keuzelijst die de verschillende filterklasses van een filterdoek voor een toestelventilator bevat."""
    naam = 'KlToestelventilatorFilterdoekKlasse'
    label = 'Toestelventilator filterdoek klasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToestelventilatorFilterdoekKlasse'
    definition = 'Keuzelijst die de verschillende filterklasses van een filterdoek voor een toestelventilator bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToestelventilatorFilterdoekKlasse'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

