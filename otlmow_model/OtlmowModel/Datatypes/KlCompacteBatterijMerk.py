# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCompacteBatterijMerk(KeuzelijstField):
    """Het merk van de compacte batterij."""
    naam = 'KlCompacteBatterijMerk'
    label = 'Compacte batterij merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCompacteBatterijMerk'
    definition = 'Het merk van de compacte batterij.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCompacteBatterijMerk'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

