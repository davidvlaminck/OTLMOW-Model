# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBrandwerendeBekleding(KeuzelijstField):
    """De verschijningsvorm of applicatiemethode van het materiaal, zoals plaat, paneel, gespoten materiaal of intumescente verf."""
    naam = 'KlTypeBrandwerendeBekleding'
    label = 'type brandwerende bekleding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBrandwerendeBekleding'
    definition = 'De verschijningsvorm of applicatiemethode van het materiaal, zoals plaat, paneel, gespoten materiaal of intumescente verf.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBrandwerendeBekleding'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

