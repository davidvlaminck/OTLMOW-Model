# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPMUModelnaam(KeuzelijstField):
    """Power management unit modelnamen."""
    naam = 'KlPMUModelnaam'
    label = 'Power management unit modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPMUModelnaam'
    definition = 'Power management unit modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPMUModelnaam'
    options = {
        'pmu701': KeuzelijstWaarde(invulwaarde='pmu701',
                                   label='PMU701',
                                   status='ingebruik',
                                   definitie='PMU701',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPMUModelnaam/pmu701')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

