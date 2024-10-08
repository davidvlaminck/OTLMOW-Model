# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSteenslagType(KeuzelijstField):
    """Steenslag types."""
    naam = 'KlSteenslagType'
    label = 'Steenslag type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSteenslagType'
    definition = 'Steenslag types.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSteenslagType'
    options = {
        'type-IA': KeuzelijstWaarde(invulwaarde='type-IA',
                                    label='type IA',
                                    status='ingebruik',
                                    definitie='type IA',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IA'),
        'type-IB': KeuzelijstWaarde(invulwaarde='type-IB',
                                    label='type IB',
                                    status='ingebruik',
                                    definitie='type IB',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IB'),
        'type-IIA': KeuzelijstWaarde(invulwaarde='type-IIA',
                                     label='type IIA',
                                     status='ingebruik',
                                     definitie='type IIA',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIA'),
        'type-IIB': KeuzelijstWaarde(invulwaarde='type-IIB',
                                     label='type IIB',
                                     status='ingebruik',
                                     definitie='type IIB',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIB'),
        'type-IIIA': KeuzelijstWaarde(invulwaarde='type-IIIA',
                                      label='type IIIA',
                                      status='ingebruik',
                                      definitie='type IIIA',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIIA'),
        'type-IIIB': KeuzelijstWaarde(invulwaarde='type-IIIB',
                                      label='type IIIB',
                                      status='ingebruik',
                                      definitie='type IIIB',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSteenslagType/type-IIIB')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

