# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTijdschakelaarUitvoering(KeuzelijstField):
    """Mogelijke uitvoeringen voor tijdschakelaars volgens de manier waarop instellingen ingegeven worden."""
    naam = 'KlTijdschakelaarUitvoering'
    label = 'Uitvoeringen tijdschakelaar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTijdschakelaarUitvoering'
    definition = 'Mogelijke uitvoeringen voor tijdschakelaars volgens de manier waarop instellingen ingegeven worden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTijdschakelaarUitvoering'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

