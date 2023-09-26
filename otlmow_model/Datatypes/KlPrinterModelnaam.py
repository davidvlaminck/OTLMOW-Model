# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPrinterModelnaam(KeuzelijstField):
    """Lijst met modelnamen van printers."""
    naam = 'KlPrinterModelnaam'
    label = 'Printer modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPrinterModelnaam'
    definition = 'Lijst met modelnamen van printers.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPrinterModelnaam'
    options = {
        'gwt': KeuzelijstWaarde(invulwaarde='gwt',
                                label='GWT',
                                status='ingebruik',
                                definitie='GWT',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPrinterModelnaam/gwt')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

