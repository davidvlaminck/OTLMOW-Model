# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSelLusVerbinding(KeuzelijstField):
    """Keuzelijst met soorten verbindingen voor selectieve lussen."""
    naam = 'KlSelLusVerbinding'
    label = 'Selectieve lus verbinding'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSelLusVerbinding'
    definition = 'Keuzelijst met soorten verbindingen voor selectieve lussen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSelLusVerbinding'
    options = {
        'contact': KeuzelijstWaarde(invulwaarde='contact',
                                    label='contact',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusVerbinding/contact'),
        'serieel': KeuzelijstWaarde(invulwaarde='serieel',
                                    label='serieel',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusVerbinding/serieel')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))
