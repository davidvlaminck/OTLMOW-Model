# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTankMateriaal(KeuzelijstField):
    """Het materiaal waaruit de tank vervaardigd is."""
    naam = 'KlTankMateriaal'
    label = 'Tank materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTankMateriaal'
    definition = 'Het materiaal waaruit de tank vervaardigd is.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTankMateriaal'
    options = {
        'rvs-304': KeuzelijstWaarde(invulwaarde='rvs-304',
                                    label='RVS 304',
                                    status='ingebruik',
                                    definitie='RVS 304',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTankMateriaal/rvs-304')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

