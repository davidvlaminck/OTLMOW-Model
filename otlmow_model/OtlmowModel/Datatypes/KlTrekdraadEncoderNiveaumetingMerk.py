# coding=utf-8
from types import MappingProxyType
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTrekdraadEncoderNiveaumetingMerk(KeuzelijstField):
    """Merknamen van de trekdraad encoder niveaumeting."""
    naam = 'KlTrekdraadEncoderNiveaumetingMerk'
    label = 'Trekdraad encoder niveaumeting merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTrekdraadEncoderNiveaumetingMerk'
    definition = 'Merknamen van de trekdraad encoder niveaumeting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTrekdraadEncoderNiveaumetingMerk'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

