# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTankMerk(KeuzelijstField):
    """Het merk van de tank."""
    naam = 'KlTankMerk'
    label = 'Tank merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTankMerk'
    definition = 'Het merk van de tank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTankMerk'
    options = {
        'idrot': KeuzelijstWaarde(invulwaarde='idrot',
                                  label='IDROT',
                                  status='ingebruik',
                                  definitie='IDROT',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankMerk/idrot')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

