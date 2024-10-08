# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPTRegelaarModuleModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor PTRegelaarModule."""
    naam = 'KlPTRegelaarModuleModelnaam'
    label = 'PT regelaarmodule modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlPTRegelaarModuleModelnaam'
    definition = 'Keuzelijst met modelnamen voor PTRegelaarModule.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPTRegelaarModuleModelnaam'
    options = {
        'arf7941ba': KeuzelijstWaarde(invulwaarde='arf7941ba',
                                      label='ARF7941BA',
                                      status='ingebruik',
                                      definitie='ARF7941BA',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/arf7941ba'),
        'cp5-241-s1': KeuzelijstWaarde(invulwaarde='cp5-241-s1',
                                       label='CP5.241-S1',
                                       status='ingebruik',
                                       definitie='CP5.241-S1',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/cp5-241-s1'),
        'nport5150a': KeuzelijstWaarde(invulwaarde='nport5150a',
                                       label='NPort5150A',
                                       status='ingebruik',
                                       definitie='NPort5150A',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/nport5150a'),
        'oas4930': KeuzelijstWaarde(invulwaarde='oas4930',
                                    label='OAS4930',
                                    status='ingebruik',
                                    definitie='OAS4930',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/oas4930'),
        'oas6010': KeuzelijstWaarde(invulwaarde='oas6010',
                                    label='OAS6010',
                                    status='ingebruik',
                                    definitie='OAS6010',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/oas6010'),
        'oas6030': KeuzelijstWaarde(invulwaarde='oas6030',
                                    label='OAS6030',
                                    status='ingebruik',
                                    definitie='OAS6030',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/oas6030'),
        'oas6040': KeuzelijstWaarde(invulwaarde='oas6040',
                                    label='OAS6040',
                                    status='ingebruik',
                                    definitie='OAS6040',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/oas6040'),
        'oas9010': KeuzelijstWaarde(invulwaarde='oas9010',
                                    label='OAS9010',
                                    status='ingebruik',
                                    definitie='OAS9010',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/oas9010'),
        'oas9110': KeuzelijstWaarde(invulwaarde='oas9110',
                                    label='OAS9110',
                                    status='ingebruik',
                                    definitie='OAS9110',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/oas9110'),
        'oas9200': KeuzelijstWaarde(invulwaarde='oas9200',
                                    label='OAS9200',
                                    status='ingebruik',
                                    definitie='OAS9200',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/oas9200'),
        'oas9210': KeuzelijstWaarde(invulwaarde='oas9210',
                                    label='OAS9210',
                                    status='ingebruik',
                                    definitie='OAS9210',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/oas9210'),
        'oas9310': KeuzelijstWaarde(invulwaarde='oas9310',
                                    label='OAS9310',
                                    status='ingebruik',
                                    definitie='OAS9310',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/oas9310'),
        'oas9330': KeuzelijstWaarde(invulwaarde='oas9330',
                                    label='OAS9330',
                                    status='ingebruik',
                                    definitie='OAS9330',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/oas9330'),
        'oas9340': KeuzelijstWaarde(invulwaarde='oas9340',
                                    label='OAS9340',
                                    status='ingebruik',
                                    definitie='OAS9340',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleModelnaam/oas9340')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

