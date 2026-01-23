# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFunctionaliteitsvereisteKabelleidingdoorvoer(KeuzelijstField):
    """De opties van de functionaliteitsvereisten voor de kabelleidingdoorvoer."""
    naam = 'KlFunctionaliteitsvereisteKabelleidingdoorvoer'
    label = 'functionaliteitsvereiste kabelleidingdoorvoer'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFunctionaliteitsvereisteKabelleidingdoorvoer'
    definition = 'De opties van de functionaliteitsvereisten voor de kabelleidingdoorvoer.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFunctionaliteitsvereisteKabelleidingdoorvoer'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

