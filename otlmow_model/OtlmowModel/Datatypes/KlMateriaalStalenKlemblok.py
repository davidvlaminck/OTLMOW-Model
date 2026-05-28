# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalStalenKlemblok(KeuzelijstField):
    """De keuzelijst van de opties van materialen voor het stalen klemblok van het klemsysteem."""
    naam = 'KlMateriaalStalenKlemblok'
    label = 'Het materiaal van het stalen klemblok'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalStalenKlemblok'
    definition = 'De keuzelijst van de opties van materialen voor het stalen klemblok van het klemsysteem.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalStalenKlemblok'
    options = {
        'constructiestaal': KeuzelijstWaarde(invulwaarde='constructiestaal',
                                             label='constructiestaal',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStalenKlemblok/constructiestaal'),
        'gietstaal': KeuzelijstWaarde(invulwaarde='gietstaal',
                                      label='gietstaal',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStalenKlemblok/gietstaal'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='RVS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStalenKlemblok/rvs'),
        'smeedstaal': KeuzelijstWaarde(invulwaarde='smeedstaal',
                                       label='smeedstaal',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStalenKlemblok/smeedstaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

