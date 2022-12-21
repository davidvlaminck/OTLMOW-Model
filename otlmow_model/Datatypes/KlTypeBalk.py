# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBalk(KeuzelijstField):
    """De soort balk."""
    naam = 'KlTypeBalk'
    label = 'Type balk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeBalk'
    definition = 'De soort balk.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBalk'
    options = {
        'balk-ligger': KeuzelijstWaarde(invulwaarde='balk-ligger',
                                        label='Balk/ligger',
                                        status='ingebruik',
                                        definitie='Een balk is een enkelvoudig ruimte-overspannend constructie-element waarvan de lengte vele malen groter is dan de breedte en de hoogte in doorsnede. De breedte is weer gelijk of kleiner dan de hoogte.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBalk/balk-ligger'),
        'koppelbalk': KeuzelijstWaarde(invulwaarde='koppelbalk',
                                       label='Koppelbalk',
                                       status='ingebruik',
                                       definitie='Een balk die de delen van een constructie met elkaar verbindt.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBalk/koppelbalk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

