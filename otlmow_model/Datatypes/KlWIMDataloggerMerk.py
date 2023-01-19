# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWIMDataloggerMerk(KeuzelijstField):
    """Het merk van de WIM-datalogger."""
    naam = 'KlWIMDataloggerMerk'
    label = 'WIM-datalogger merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWIMDataloggerMerk'
    definition = 'Het merk van de WIM-datalogger.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWIMDataloggerMerk'
    options = {
        'kistler': KeuzelijstWaarde(invulwaarde='kistler',
                                    label='Kistler',
                                    status='ingebruik',
                                    definitie='Kistler',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWIMDataloggerMerk/kistler')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

