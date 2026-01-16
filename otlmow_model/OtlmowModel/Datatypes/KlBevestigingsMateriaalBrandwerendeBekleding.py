# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBevestigingsMateriaalBrandwerendeBekleding(KeuzelijstField):
    """Keuzelijst met het type materiaal van de ankers, bouten of andere middelen waarmee de bekleding is bevestigd."""
    naam = 'KlBevestigingsMateriaalBrandwerendeBekleding'
    label = 'bevestigingsmateriaal brandwerende bekleding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBevestigingsMateriaalBrandwerendeBekleding'
    definition = 'Keuzelijst met het type materiaal van de ankers, bouten of andere middelen waarmee de bekleding is bevestigd.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBevestigingsMateriaalBrandwerendeBekleding'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

