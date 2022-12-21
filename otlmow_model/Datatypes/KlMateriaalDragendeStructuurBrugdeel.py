# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalDragendeStructuurBrugdeel(KeuzelijstField):
    """Het materiaal waaruit de dragende structuur van het brugdeel is opgebouwd."""
    naam = 'KlMateriaalDragendeStructuurBrugdeel'
    label = 'Materiaal dragende structuur brugdeel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMateriaalDragendeStructuurBrugdeel'
    definition = 'Het materiaal waaruit de dragende structuur van het brugdeel is opgebouwd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalDragendeStructuurBrugdeel'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='Beton',
                                  status='ingebruik',
                                  definitie='Beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDragendeStructuurBrugdeel/beton'),
        'gegolfd-plaatstaal': KeuzelijstWaarde(invulwaarde='gegolfd-plaatstaal',
                                               label='Gegolfd plaatstaal',
                                               status='ingebruik',
                                               definitie='Gegolfd plaatstaal',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDragendeStructuurBrugdeel/gegolfd-plaatstaal'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='Hout',
                                 status='ingebruik',
                                 definitie='Hout',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDragendeStructuurBrugdeel/hout'),
        'metselwerk': KeuzelijstWaarde(invulwaarde='metselwerk',
                                       label='Metselwerk',
                                       status='ingebruik',
                                       definitie='Metselwerk',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDragendeStructuurBrugdeel/metselwerk'),
        'mixte-staal-en-beton': KeuzelijstWaarde(invulwaarde='mixte-staal-en-beton',
                                                 label='Mixte (staal en beton)',
                                                 status='ingebruik',
                                                 definitie='Mixte (staal en beton)',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDragendeStructuurBrugdeel/mixte-staal-en-beton'),
        'natuursteen': KeuzelijstWaarde(invulwaarde='natuursteen',
                                        label='Natuursteen',
                                        status='ingebruik',
                                        definitie='Natuursteen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDragendeStructuurBrugdeel/natuursteen'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='Staal',
                                  status='ingebruik',
                                  definitie='Staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDragendeStructuurBrugdeel/staal'),
        'voorgebogen-liggers': KeuzelijstWaarde(invulwaarde='voorgebogen-liggers',
                                                label='Voorgebogen liggers',
                                                status='ingebruik',
                                                definitie='Voorgebogen liggers',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDragendeStructuurBrugdeel/voorgebogen-liggers')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

