# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkMerk(KeuzelijstField):
    """Merknamen voor Netwerkelementen."""
    naam = 'KlNetwerkMerk'
    label = 'Netwerkelement merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkMerk'
    definition = 'Merknamen voor Netwerkelementen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkMerk'
    options = {
        'ABB': KeuzelijstWaarde(invulwaarde='ABB',
                                label='ABB',
                                status='ingebruik',
                                definitie='ABB',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/ABB'),
        'Ciena': KeuzelijstWaarde(invulwaarde='Ciena',
                                  label='Ciena',
                                  status='ingebruik',
                                  definitie='Ciena',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Ciena'),
        'Cisco': KeuzelijstWaarde(invulwaarde='Cisco',
                                  label='Cisco',
                                  status='ingebruik',
                                  definitie='Cisco',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Cisco'),
        'HP': KeuzelijstWaarde(invulwaarde='HP',
                               label='HP',
                               status='ingebruik',
                               definitie='HP',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/HP'),
        'NOKIA': KeuzelijstWaarde(invulwaarde='NOKIA',
                                  label='NOKIA',
                                  status='ingebruik',
                                  definitie='NOKIA',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/NOKIA'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 status='ingebruik',
                                 definitie='null',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/NULL'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  status='ingebruik',
                                  definitie='Deze optie mag uitsluitend TIJDELIJK worden gebruikt en enkel tot de juiste gegevens beschikbaar zijn. Misbruik van deze optie leidt tot verminderde datakwaliteit.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Other'),
        'Proxim': KeuzelijstWaarde(invulwaarde='Proxim',
                                   label='Proxim',
                                   status='ingebruik',
                                   definitie='Proxim',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Proxim'),
        'actelis': KeuzelijstWaarde(invulwaarde='actelis',
                                    label='Actelis',
                                    status='ingebruik',
                                    definitie='Actelis',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/actelis'),
        'aerohive': KeuzelijstWaarde(invulwaarde='aerohive',
                                     label='Aerohive',
                                     status='ingebruik',
                                     definitie='Aerohive',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/aerohive'),
        'edge': KeuzelijstWaarde(invulwaarde='edge',
                                 label='Edge',
                                 status='ingebruik',
                                 definitie='Edge',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/edge'),
        'fortinet': KeuzelijstWaarde(invulwaarde='fortinet',
                                     label='Fortinet',
                                     status='ingebruik',
                                     definitie='Fortinet',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/fortinet'),
        'hirschmann': KeuzelijstWaarde(invulwaarde='hirschmann',
                                       label='Hirschmann',
                                       status='ingebruik',
                                       definitie='Hirschmann',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/hirschmann'),
        'hiveap-122': KeuzelijstWaarde(invulwaarde='hiveap-122',
                                       label='HiveAP 122',
                                       status='verwijderd',
                                       definitie='HiveAP 122',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/hiveap-122'),
        'oring': KeuzelijstWaarde(invulwaarde='oring',
                                  label='Oring',
                                  status='ingebruik',
                                  definitie='Oring',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/oring')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

