# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDetectiecameraModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Detectiecamera."""
    naam = 'KlDetectiecameraModelnaam'
    label = 'Detectiecamera modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDetectiecameraModelnaam'
    definition = 'Keuzelijst met modelnamen voor Detectiecamera.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectiecameraModelnaam'
    options = {
        'thermicam-ai-345': KeuzelijstWaarde(invulwaarde='thermicam-ai-345',
                                             label='ThermiCam AI-345',
                                             status='ingebruik',
                                             definitie='ThermiCam AI-345',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraModelnaam/thermicam-ai-345'),
        'thermicam-ai-635': KeuzelijstWaarde(invulwaarde='thermicam-ai-635',
                                             label='ThermiCam AI-635',
                                             status='ingebruik',
                                             definitie='ThermiCam AI-635',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraModelnaam/thermicam-ai-635'),
        'thermicam-ai-690': KeuzelijstWaarde(invulwaarde='thermicam-ai-690',
                                             label='ThermiCam AI-690',
                                             status='ingebruik',
                                             definitie='ThermiCam AI-690',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraModelnaam/thermicam-ai-690'),
        'thermicam2-390': KeuzelijstWaarde(invulwaarde='thermicam2-390',
                                           label='ThermiCam2 390',
                                           status='ingebruik',
                                           definitie='ThermiCam2 390',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraModelnaam/thermicam2-390'),
        'traficam-ai-narrow': KeuzelijstWaarde(invulwaarde='traficam-ai-narrow',
                                               label='TrafiCam AI – Narrow',
                                               status='ingebruik',
                                               definitie='TrafiCam AI – Narrow',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraModelnaam/traficam-ai-narrow'),
        'traficam-ai-wide': KeuzelijstWaarde(invulwaarde='traficam-ai-wide',
                                             label='TrafiCam AI - Wide',
                                             status='ingebruik',
                                             definitie='TrafiCam AI - Wide',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraModelnaam/traficam-ai-wide'),
        'traficam-x-stream2-bpl-narrow': KeuzelijstWaarde(invulwaarde='traficam-x-stream2-bpl-narrow',
                                                          label='TrafiCam X-stream2 BPL Narrow',
                                                          status='ingebruik',
                                                          definitie='TrafiCam X-stream2 BPL Narrow',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraModelnaam/traficam-x-stream2-bpl-narrow'),
        'traficam-x-stream2-bpl-wide': KeuzelijstWaarde(invulwaarde='traficam-x-stream2-bpl-wide',
                                                        label='TrafiCam X-stream2 BPL Wide',
                                                        status='ingebruik',
                                                        definitie='TrafiCam X-stream2 BPL Wide',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraModelnaam/traficam-x-stream2-bpl-wide'),
        'traficam2-narrow-angle': KeuzelijstWaarde(invulwaarde='traficam2-narrow-angle',
                                                   label='TrafiCam2 Narrow Angle',
                                                   status='ingebruik',
                                                   definitie='TrafiCam2 Narrow Angle',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraModelnaam/traficam2-narrow-angle'),
        'traficam2-wide-angle': KeuzelijstWaarde(invulwaarde='traficam2-wide-angle',
                                                 label='TrafiCam2 Wide Angle',
                                                 status='ingebruik',
                                                 definitie='TrafiCam2 Wide Angle',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectiecameraModelnaam/traficam2-wide-angle')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

