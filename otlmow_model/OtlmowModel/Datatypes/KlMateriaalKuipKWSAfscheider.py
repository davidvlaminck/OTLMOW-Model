# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalKuipKWSAfscheider(KeuzelijstField):
    """De verschillende types materialen waaruit de vloeistofdichte kuip van de KWS afscheider kan vervaardigd zijn."""
    naam = 'KlMateriaalKuipKWSAfscheider'
    label = 'Materiaal kuip KWS Afscheider'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalKuipKWSAfscheider'
    definition = 'De verschillende types materialen waaruit de vloeistofdichte kuip van de KWS afscheider kan vervaardigd zijn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalKuipKWSAfscheider'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

