# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOperationeleStatus(KeuzelijstField):
    """Operationele status codes."""
    naam = 'KlOperationeleStatus'
    label = 'Keuzelijst operationele status'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOperationeleStatus'
    definition = 'Operationele status codes.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOperationeleStatus'
    options = {
        'actief': KeuzelijstWaarde(invulwaarde='actief',
                                   label='actief',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief'),
        'actief-met-geplande-verwijdering': KeuzelijstWaarde(invulwaarde='actief-met-geplande-verwijdering',
                                                             label='actief met geplande verwijdering',
                                                             status='ingebruik',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief-met-geplande-verwijdering'),
        'actief-met-geplande-wijziging': KeuzelijstWaarde(invulwaarde='actief-met-geplande-wijziging',
                                                          label='actief met geplande wijziging',
                                                          status='ingebruik',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief-met-geplande-wijziging'),
        'actief-met-tijdelijke-wijziging': KeuzelijstWaarde(invulwaarde='actief-met-tijdelijke-wijziging',
                                                            label='actief met tijdelijke wijziging',
                                                            status='ingebruik',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/actief-met-tijdelijke-wijziging'),
        'tijdelijk-actief': KeuzelijstWaarde(invulwaarde='tijdelijk-actief',
                                             label='tijdelijk actief',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/tijdelijk-actief'),
        'tijdelijk-inactief': KeuzelijstWaarde(invulwaarde='tijdelijk-inactief',
                                               label='tijdelijk inactief',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOperationeleStatus/tijdelijk-inactief')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

