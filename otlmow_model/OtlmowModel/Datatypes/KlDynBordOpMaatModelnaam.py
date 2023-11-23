# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordOpMaatModelnaam(KeuzelijstField):
    """Keuzelijst met de gangbare modelnamen van dynamische borden op maat. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""
    naam = 'KlDynBordOpMaatModelnaam'
    label = 'Keuzelijst modelnamen voor dynamische borden op maat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordOpMaatModelnaam'
    definition = 'Keuzelijst met de gangbare modelnamen van dynamische borden op maat. De modelnamen worden meestal door de leverancier of fabrikant bepaald.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordOpMaatModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

