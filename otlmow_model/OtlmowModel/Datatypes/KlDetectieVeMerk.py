# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDetectieVeMerk(KeuzelijstField):
    """De mogelijke opties voor het merk van een detectieverwerkingseenheid."""
    naam = 'KlDetectieVeMerk'
    label = 'Detectieverwerkingseenheid merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDetectieVeMerk'
    definition = 'De mogelijke opties voor het merk van een detectieverwerkingseenheid.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectieVeMerk'
    options = {
        'flir': KeuzelijstWaarde(invulwaarde='flir',
                                 label='FLIR',
                                 status='ingebruik',
                                 definitie='FLIR',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectieVeMerk/flir')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

