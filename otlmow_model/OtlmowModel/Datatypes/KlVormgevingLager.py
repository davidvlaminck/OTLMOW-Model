# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVormgevingLager(KeuzelijstField):
    """Mogelijke vormen"""
    naam = 'KlVormgevingLager'
    label = 'Vormgeving'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormgevingLager'
    definition = 'Mogelijke vormen'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormgevingLager'
    options = {
        'axiale-lager': KeuzelijstWaarde(invulwaarde='axiale-lager',
                                         label='axiale lager',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormgevingLager/axiale-lager'),
        'cilindrische-lager': KeuzelijstWaarde(invulwaarde='cilindrische-lager',
                                               label='cilindrische lager',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormgevingLager/cilindrische-lager'),
        'radiale-sferische-lager-(gewrichtslager)': KeuzelijstWaarde(invulwaarde='radiale-sferische-lager-(gewrichtslager)',
                                                                     label='radiale sferische lager (gewrichtslager)',
                                                                     status='ingebruik',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormgevingLager/radiale-sferische-lager-(gewrichtslager)'),
        'sferische-lager': KeuzelijstWaarde(invulwaarde='sferische-lager',
                                            label='sferische lager',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormgevingLager/sferische-lager')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

