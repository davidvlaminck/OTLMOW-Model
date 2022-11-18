# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIBaseline(KeuzelijstField):
    """De specificatieversie van het protocol van de iVRI component."""
    naam = 'KlIVRIBaseline'
    label = 'iVRIBaseline'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlIVRIBaseline'
    definition = 'De specificatieversie van het protocol van de iVRI component.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIBaseline'
    options = {
        'idd-tlc-fi-version-1-3-1': KeuzelijstWaarde(invulwaarde='idd-tlc-fi-version-1-3-1',
                                                     label='IDD TLC-FI version 1.3.1',
                                                     status='ingebruik',
                                                     definitie='IDD TLC-FI version 1.3.1',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIBaseline/idd-tlc-fi-version-1-3-1')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

