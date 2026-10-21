# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKleurStandaard(KeuzelijstField):
    """De mogelijke standaard (RAL) kleuren die gekozen kunnen worden."""
    naam = 'KlKleurStandaard'
    label = 'Kleur standaard'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlKleurStandaard'
    definition = 'De mogelijke standaard (RAL) kleuren die gekozen kunnen worden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKleurStandaard'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

