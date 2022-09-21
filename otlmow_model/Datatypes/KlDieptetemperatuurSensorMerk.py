# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDieptetemperatuurSensorMerk(KeuzelijstField):
    """Dieptetemperatuursensor merken."""
    naam = 'KlDieptetemperatuurSensorMerk'
    label = 'Dieptetemperatuursensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDieptetemperatuurSensorMerk'
    definition = 'Dieptetemperatuursensor merken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDieptetemperatuurSensorMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

