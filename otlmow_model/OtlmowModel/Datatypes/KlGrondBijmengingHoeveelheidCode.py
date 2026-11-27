# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrondBijmengingHoeveelheidCode(KeuzelijstField):
    """De mogelijke waarden voor de hoeveelheid bijmenging (X staat voor de lithologie van de bijmenging)."""
    naam = 'KlGrondBijmengingHoeveelheidCode'
    label = 'Grondbijmenging hoeveelheidscode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGrondBijmengingHoeveelheidCode'
    definition = 'De mogelijke waarden voor de hoeveelheid bijmenging (X staat voor de lithologie van de bijmenging).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrondBijmengingHoeveelheidCode'
    options: MappingProxyType = MappingProxyType({
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

