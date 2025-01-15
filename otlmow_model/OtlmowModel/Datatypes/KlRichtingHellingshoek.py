# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRichtingHellingshoek(KeuzelijstField):
    """Keuzelijst met te opties van de richting van de hellingshoek."""
    naam = 'KlRichtingHellingshoek'
    label = 'keuzelijst richting hellingshoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRichtingHellingshoek'
    definition = 'Keuzelijst met te opties van de richting van de hellingshoek.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRichtingHellingshoek'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

