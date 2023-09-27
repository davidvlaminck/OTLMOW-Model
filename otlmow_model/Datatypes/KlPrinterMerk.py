# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPrinterMerk(KeuzelijstField):
    """Lijst met merknamen van printers."""
    naam = 'KlPrinterMerk'
    label = 'Printer merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPrinterMerk'
    definition = 'Lijst met merknamen van printers.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPrinterMerk'
    options = {
        'pr3221-125t-c3': KeuzelijstWaarde(invulwaarde='pr3221-125t-c3',
                                           label='PR3221/125t C3',
                                           status='ingebruik',
                                           definitie='PR3221/125t C3',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPrinterMerk/pr3221-125t-c3')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

