# coding=utf-8
from types import MappingProxyType
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTandwielkastMerk(KeuzelijstField):
    """Lijst van merknamen van tandwielkasten volgens de fabrikant."""
    naam = 'KlTandwielkastMerk'
    label = 'Merknamen tandwielkasten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTandwielkastMerk'
    definition = 'Lijst van merknamen van tandwielkasten volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTandwielkastMerk'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

