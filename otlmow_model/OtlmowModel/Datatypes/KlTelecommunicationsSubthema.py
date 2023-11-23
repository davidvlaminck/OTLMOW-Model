# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTelecommunicationsSubthema(KeuzelijstField):
    """Lijst voor classificatie van een kabels en appurtenance voor telecommunicatie."""
    naam = 'KlTelecommunicationsSubthema'
    label = 'Telecommunications subthema'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTelecommunicationsSubthema'
    definition = 'Lijst voor classificatie van een kabels en appurtenance voor telecommunicatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTelecommunicationsSubthema'
    options = {
        'elektronischecommunicatie': KeuzelijstWaarde(invulwaarde='elektronischecommunicatie',
                                                      label='elektronischeCommunicatie',
                                                      status='ingebruik',
                                                      definitie='elektronischeCommunicatie',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecommunicationsSubthema/elektronischecommunicatie')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

