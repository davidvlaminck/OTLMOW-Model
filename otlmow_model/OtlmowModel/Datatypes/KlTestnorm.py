# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTestnorm(KeuzelijstField):
    """Keuzelijst met de normen of standaarden (bv. NBN EN 13501) volgens dewelke de brandwerende eigenschappen van het materiaal zijn getest en gecertificeerd."""
    naam = 'KlTestnorm'
    label = 'testnorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTestnorm'
    definition = 'Keuzelijst met de normen of standaarden (bv. NBN EN 13501) volgens dewelke de brandwerende eigenschappen van het materiaal zijn getest en gecertificeerd.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTestnorm'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

