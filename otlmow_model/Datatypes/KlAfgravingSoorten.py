# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfgravingSoorten(KeuzelijstField):
    """De specificatie van type handeling bij afgraving."""
    naam = 'KlAfgravingSoorten'
    label = 'Afgraving soorten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlAfgravingSoorten'
    definition = 'De specificatie van type handeling bij afgraving.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfgravingSoorten'
    options = {
        '20-cm': KeuzelijstWaarde(invulwaarde='20-cm',
                                  label='20 cm',
                                  status='ingebruik',
                                  definitie='De afgraving met vaste dikte (E = 20 cm) omvat het wegnemen van de bouwlaag van bedding, taluds, ondervlak, dijken en/of bermen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfgravingSoorten/20-cm'),
        'op-veranderlijke-dikte': KeuzelijstWaarde(invulwaarde='op-veranderlijke-dikte',
                                                   label='op veranderlijke dikte',
                                                   status='ingebruik',
                                                   definitie='De afgraving op veranderlijke dikte omvat het wegnemen van de bouwlaag van bedding, taluds, ondervlak, dijken en/of bermen.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfgravingSoorten/op-veranderlijke-dikte'),
        'plaatselijke-uitvoering': KeuzelijstWaarde(invulwaarde='plaatselijke-uitvoering',
                                                    label='plaatselijke uitvoering',
                                                    status='ingebruik',
                                                    definitie='De afgraving in plaatselijke uitvoering omvat het wegnemen van de bouwlaag van bedding, taluds, ondervlak, dijken en/of bermen.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfgravingSoorten/plaatselijke-uitvoering')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

