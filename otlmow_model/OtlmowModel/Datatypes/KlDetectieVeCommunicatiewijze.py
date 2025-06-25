# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDetectieVeCommunicatiewijze(KeuzelijstField):
    """De mogelijke opties voor de communicatiewijze van een detectieverwerkingseenheid."""
    naam = 'KlDetectieVeCommunicatiewijze'
    label = 'Detectie verwerkingseenheid communicatiewijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDetectieVeCommunicatiewijze'
    definition = 'De mogelijke opties voor de communicatiewijze van een detectieverwerkingseenheid.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectieVeCommunicatiewijze'
    options = {
        'detection-output': KeuzelijstWaarde(invulwaarde='detection-output',
                                             label='detection output',
                                             status='ingebruik',
                                             definitie='detection output',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectieVeCommunicatiewijze/detection-output')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

