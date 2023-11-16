# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGewaarborgdeWrijvingshoek(KeuzelijstField):
    """De hoek van inwendige wrijving geeft een aanwijzing omtrent de afschuifkarakteristieken en wordt dan ook gebruikt bij berekening van afschuiving, gronddruk en draagvermogen van paalfunderingen."""
    naam = 'KlGewaarborgdeWrijvingshoek'
    label = 'Gewaarborgde wrijvingshoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlGewaarborgdeWrijvingshoek'
    definition = 'De hoek van inwendige wrijving geeft een aanwijzing omtrent de afschuifkarakteristieken en wordt dan ook gebruikt bij berekening van afschuiving, gronddruk en draagvermogen van paalfunderingen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGewaarborgdeWrijvingshoek'
    options = {
        '25-graden': KeuzelijstWaarde(invulwaarde='25-graden',
                                      label='25 graden',
                                      status='ingebruik',
                                      definitie='De hoek van inwendige wrijving van 25 graden.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGewaarborgdeWrijvingshoek/25-graden'),
        '27-graden': KeuzelijstWaarde(invulwaarde='27-graden',
                                      label='27 graden',
                                      status='ingebruik',
                                      definitie='De hoek van inwendige wrijving van 27 graden.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGewaarborgdeWrijvingshoek/27-graden'),
        '30-graden': KeuzelijstWaarde(invulwaarde='30-graden',
                                      label='30 graden',
                                      status='ingebruik',
                                      definitie='De hoek van inwendige wrijving van 30 graden.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGewaarborgdeWrijvingshoek/30-graden'),
        '32-5-graden': KeuzelijstWaarde(invulwaarde='32-5-graden',
                                        label='32.5 graden',
                                        status='ingebruik',
                                        definitie='De hoek van inwendige wrijving van 32.5 graden.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGewaarborgdeWrijvingshoek/32-5-graden'),
        '35-graden': KeuzelijstWaarde(invulwaarde='35-graden',
                                      label='35 graden',
                                      status='ingebruik',
                                      definitie='De hoek van inwendige wrijving van 35 graden.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGewaarborgdeWrijvingshoek/35-graden')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

