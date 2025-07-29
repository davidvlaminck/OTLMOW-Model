# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStangHydraulischeCilinderBekleding(KeuzelijstField):
    """Keuzelijst voor de soorten bekleding voor een stang van een hydraulishe cilinder."""
    naam = 'KlStangHydraulischeCilinderBekleding'
    label = 'Stang hydraulische cilinder bekleding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStangHydraulischeCilinderBekleding'
    definition = 'Keuzelijst voor de soorten bekleding voor een stang van een hydraulishe cilinder.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStangHydraulischeCilinderBekleding'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

