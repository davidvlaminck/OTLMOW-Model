# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPtKARModemProtocol(KeuzelijstField):
    """Beschrijft het protocol dat de PT-KAR-Modem gebruikt om te communiceren."""
    naam = 'KlPtKARModemProtocol'
    label = 'PT-KAR-modem protocol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPtKARModemProtocol'
    definition = 'Beschrijft het protocol dat de PT-KAR-Modem gebruikt om te communiceren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPtKARModemProtocol'
    options = {
        'daiser': KeuzelijstWaarde(invulwaarde='daiser',
                                   label='DAISER',
                                   status='ingebruik',
                                   definitie='DAISER',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtKARModemProtocol/daiser'),
        'r09-16': KeuzelijstWaarde(invulwaarde='r09-16',
                                   label='R09.16',
                                   status='ingebruik',
                                   definitie='R09.16',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPtKARModemProtocol/r09-16')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

