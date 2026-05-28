# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeVullingBalg(KeuzelijstField):
    """Lijst met de verschillende types vulling van een balg"""
    naam = 'KlTypeVullingBalg'
    label = 'Type vulling balg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeVullingBalg'
    definition = 'Lijst met de verschillende types vulling van een balg'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeVullingBalg'
    options = {
        'lucht': KeuzelijstWaarde(invulwaarde='lucht',
                                  label='lucht',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVullingBalg/lucht'),
        'water': KeuzelijstWaarde(invulwaarde='water',
                                  label='water',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeVullingBalg/water')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

