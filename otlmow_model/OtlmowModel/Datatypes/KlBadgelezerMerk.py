# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBadgelezerMerk(KeuzelijstField):
    """Lijst van merknamen voor badgelezer volgens de fabrikant."""
    naam = 'KlBadgelezerMerk'
    label = 'Merknamen badgelezers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBadgelezerMerk'
    definition = 'Lijst van merknamen voor badgelezer volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBadgelezerMerk'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

