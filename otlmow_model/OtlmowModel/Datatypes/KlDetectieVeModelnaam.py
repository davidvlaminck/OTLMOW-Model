# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDetectieVeModelnaam(KeuzelijstField):
    """De mogelijke opties voor de modelnaam van een detectieverwerkingseenheid."""
    naam = 'KlDetectieVeModelnaam'
    label = 'Detectieverwerkingseenheid modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDetectieVeModelnaam'
    definition = 'De mogelijke opties voor de modelnaam van een detectieverwerkingseenheid.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectieVeModelnaam'
    options = {
        'ti-bpl3': KeuzelijstWaarde(invulwaarde='ti-bpl3',
                                    label='TI BPL3',
                                    status='ingebruik',
                                    definitie='TI BPL3',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectieVeModelnaam/ti-bpl3')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

