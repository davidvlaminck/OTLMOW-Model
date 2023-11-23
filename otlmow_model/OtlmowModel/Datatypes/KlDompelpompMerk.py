# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDompelpompMerk(KeuzelijstField):
    """Lijst van merknamen van dompelpompen volgens de fabrikant."""
    naam = 'KlDompelpompMerk'
    label = 'Merknamen dompelpompen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDompelpompMerk'
    definition = 'Lijst van merknamen van dompelpompen volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDompelpompMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

