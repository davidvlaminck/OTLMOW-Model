# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZuilTGCMerk(KeuzelijstField):
    """Lijst van merknamen van zuilen voor toegangscontrole volgens de fabrikant."""
    naam = 'KlZuilTGCMerk'
    label = 'Merknamen zuilen toegangscontrole'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZuilTGCMerk'
    definition = 'Lijst van merknamen van zuilen voor toegangscontrole volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZuilTGCMerk'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

