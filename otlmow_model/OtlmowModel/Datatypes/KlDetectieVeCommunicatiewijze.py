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
        'contacten': KeuzelijstWaarde(invulwaarde='contacten',
                                      label='contacten',
                                      status='ingebruik',
                                      definitie='Een communicatiewijze door middel van relais, die een schakelcontact opent of sluit.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectieVeCommunicatiewijze/contacten'),
        'detection-output': KeuzelijstWaarde(invulwaarde='detection-output',
                                             label='detection output',
                                             status='uitgebruik',
                                             definitie='detection output',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectieVeCommunicatiewijze/detection-output'),
        'serieel': KeuzelijstWaarde(invulwaarde='serieel',
                                    label='serieel',
                                    status='ingebruik',
                                    definitie='Een communicatiewijze waarbij bits van informatie één voor één worden doorgestuurd.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectieVeCommunicatiewijze/serieel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

