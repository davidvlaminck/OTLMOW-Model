# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfmetingsensorMerk(KeuzelijstField):
    """Het merk van de afmetingsensor."""
    naam = 'KlAfmetingsensorMerk'
    label = 'Afmetingsensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfmetingsensorMerk'
    definition = 'Het merk van de afmetingsensor.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfmetingsensorMerk'
    options = {
        'Sick': KeuzelijstWaarde(invulwaarde='Sick',
                                 label='Sick',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfmetingsensorMerk/Sick')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

