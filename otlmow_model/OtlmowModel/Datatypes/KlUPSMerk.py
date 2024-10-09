# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUPSMerk(KeuzelijstField):
    """Het merk van de UPS."""
    naam = 'KlUPSMerk'
    label = 'UPS merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUPSMerk'
    definition = 'Het merk van de UPS.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUPSMerk'
    options = {
        'apc': KeuzelijstWaarde(invulwaarde='apc',
                                label='APC',
                                status='ingebruik',
                                definitie='APC',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSMerk/apc'),
        'delta': KeuzelijstWaarde(invulwaarde='delta',
                                  label='Delta',
                                  status='ingebruik',
                                  definitie='Delta',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSMerk/delta'),
        'other': KeuzelijstWaarde(invulwaarde='other',
                                  label='Other',
                                  status='ingebruik',
                                  definitie='Deze optie mag uitsluitend TIJDELIJK worden gebruikt en enkel tot de juiste gegevens beschikbaar zijn. Misbruik van deze optie leidt tot verminderde datakwaliteit.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSMerk/other'),
        'phoenix-contact': KeuzelijstWaarde(invulwaarde='phoenix-contact',
                                            label='Phoenix Contact',
                                            status='ingebruik',
                                            definitie='Phoenix Contact',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSMerk/phoenix-contact'),
        'prostar': KeuzelijstWaarde(invulwaarde='prostar',
                                    label='Prostar',
                                    status='ingebruik',
                                    definitie='Prostar',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSMerk/prostar'),
        'pulse-dimension': KeuzelijstWaarde(invulwaarde='pulse-dimension',
                                            label='Pulse Dimension',
                                            status='ingebruik',
                                            definitie='Pulse Dimension',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUPSMerk/pulse-dimension')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

