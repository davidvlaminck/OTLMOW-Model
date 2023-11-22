# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeOndergrond(KeuzelijstField):
    """Keuzelijst om bij te houden welke ondergrond zich onder het koker element bevindt."""
    naam = 'KlTypeOndergrond'
    label = 'Type ondergrond'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeOndergrond'
    definition = 'Keuzelijst om bij te houden welke ondergrond zich onder het koker element bevindt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeOndergrond'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)
