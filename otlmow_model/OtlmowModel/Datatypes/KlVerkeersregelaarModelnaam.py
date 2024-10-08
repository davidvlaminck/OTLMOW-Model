# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Verkeersregelaar."""
    naam = 'KlVerkeersregelaarModelnaam'
    label = 'verkeersregelaar modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarModelnaam'
    definition = 'Keuzelijst met modelnamen voor Verkeersregelaar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarModelnaam'
    options = {
        'c9': KeuzelijstWaarde(invulwaarde='c9',
                               label='C9',
                               status='ingebruik',
                               definitie='C9',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarModelnaam/c9'),
        'civa-2020': KeuzelijstWaarde(invulwaarde='civa-2020',
                                      label='CIVA 2020',
                                      status='ingebruik',
                                      definitie='CIVA 2020',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarModelnaam/civa-2020'),
        'flow-node': KeuzelijstWaarde(invulwaarde='flow-node',
                                      label='FlowNode',
                                      status='ingebruik',
                                      definitie='FlowNode',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarModelnaam/flow-node'),
        'itc-3': KeuzelijstWaarde(invulwaarde='itc-3',
                                  label='ITC-3',
                                  status='ingebruik',
                                  definitie='ITC-3',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarModelnaam/itc-3'),
        'sx': KeuzelijstWaarde(invulwaarde='sx',
                               label='SX',
                               status='ingebruik',
                               definitie='SX',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarModelnaam/sx')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

