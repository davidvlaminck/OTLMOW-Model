# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeschermingWapeningType(KeuzelijstField):
    """De mogelijke wapeningen gebruikt bij de oa. fundering (wapeningsnet,geotextiel,geogrids)."""
    naam = 'KlBeschermingWapeningType'
    label = 'Bescherming wapening type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermingWapeningType'
    definition = 'De mogelijke wapeningen gebruikt bij de oa. fundering (wapeningsnet,geotextiel,geogrids).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermingWapeningType'
    options = {
        'gelast-geplastificeerd-gaas': KeuzelijstWaarde(invulwaarde='gelast-geplastificeerd-gaas',
                                                        label='gelast geplastificeerd gaas',
                                                        status='ingebruik',
                                                        definitie='gelast geplastificeerd gaas',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/gelast-geplastificeerd-gaas'),
        'geogrids': KeuzelijstWaarde(invulwaarde='geogrids',
                                     label='geogrids',
                                     status='ingebruik',
                                     definitie='Een roosterweefsel dat als een soort funderingsrooster wordt toegepast',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/geogrids'),
        'honinggraatstructuur': KeuzelijstWaarde(invulwaarde='honinggraatstructuur',
                                                 label='honinggraatstructuur',
                                                 status='ingebruik',
                                                 definitie='Een wapening_bescherming met honinggraatstructuur.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/honinggraatstructuur'),
        'wapeningsnet': KeuzelijstWaarde(invulwaarde='wapeningsnet',
                                         label='wapeningsnet',
                                         status='ingebruik',
                                         definitie='Keuzelijst voor de wapening gebruikt bij de fundering (wapeningsnet,geotextiel,geogrids)',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingWapeningType/wapeningsnet')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

