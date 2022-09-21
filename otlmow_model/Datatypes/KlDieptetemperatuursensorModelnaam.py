# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDieptetemperatuursensorModelnaam(KeuzelijstField):
    """Dieptetemperatuursensor modelnamen."""
    naam = 'KlDieptetemperatuursensorModelnaam'
    label = 'Dieptetemperatuursensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDieptetemperatuursensorModelnaam'
    definition = 'Dieptetemperatuursensor modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDieptetemperatuursensorModelnaam'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

