# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOrientatieKabelleidingdoorvoer(KeuzelijstField):
    """De verschillende opties van de oriëntatie van de kabelleidingdoorvoer."""
    naam = 'KlOrientatieKabelleidingdoorvoer'
    label = 'orientatie kabelleidingdoorvoer'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOrientatieKabelleidingdoorvoer'
    definition = 'De verschillende opties van de oriëntatie van de kabelleidingdoorvoer.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOrientatieKabelleidingdoorvoer'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

