# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVrStuurkaartCommunicatieprotocol(KeuzelijstField):
    """Keuzelist met de voorkomende communicatieprotocollen voor VRIstuurkaarten."""
    naam = 'KlVrStuurkaartCommunicatieprotocol'
    label = 'VRI-communicatieprotocol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVrStuurkaartCommunicatieprotocol'
    definition = 'Keuzelist met de voorkomende communicatieprotocollen voor VRIstuurkaarten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVrStuurkaartCommunicatieprotocol'
    options = {
        'canto': KeuzelijstWaarde(invulwaarde='canto',
                                  label='canto',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVrStuurkaartCommunicatieprotocol/canto'),
        'gecombineerd': KeuzelijstWaarde(invulwaarde='gecombineerd',
                                         label='gecombineerd',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVrStuurkaartCommunicatieprotocol/gecombineerd'),
        'ocit': KeuzelijstWaarde(invulwaarde='ocit',
                                 label='ocit',
                                 status='ingebruik',
                                 definitie='nog in te vullen',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVrStuurkaartCommunicatieprotocol/ocit')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

