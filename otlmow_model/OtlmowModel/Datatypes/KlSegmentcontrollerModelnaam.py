# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSegmentcontrollerModelnaam(KeuzelijstField):
    """De mogelijke modelnamen voor een segmentcontroller."""
    naam = 'KlSegmentcontrollerModelnaam'
    label = 'Segmentcontroller modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSegmentcontrollerModelnaam'
    definition = 'De mogelijke modelnamen voor een segmentcontroller.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSegmentcontrollerModelnaam'
    options = {
        'aps-g3-eth-ea': KeuzelijstWaarde(invulwaarde='aps-g3-eth-ea',
                                          label='APS-G3-ETH-EA',
                                          status='ingebruik',
                                          definitie='APS-G3-ETH-EA',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSegmentcontrollerModelnaam/aps-g3-eth-ea'),
        'aps-g3-sim-ea': KeuzelijstWaarde(invulwaarde='aps-g3-sim-ea',
                                          label='APS-G3-SIM-EA',
                                          status='ingebruik',
                                          definitie='APS-G3-SIM-EA',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSegmentcontrollerModelnaam/aps-g3-sim-ea'),
        'aps-g3-sim-ia': KeuzelijstWaarde(invulwaarde='aps-g3-sim-ia',
                                          label='APS-G3-SIM-IA',
                                          status='ingebruik',
                                          definitie='APS-G3-SIM-IA',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSegmentcontrollerModelnaam/aps-g3-sim-ia')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

