# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAanplantingswijzeSierbeplanting(KeuzelijstField):
    """De mogelijke manieren van aanplanten van sierbeplanting."""
    naam = 'KlAanplantingswijzeSierbeplanting'
    label = 'aanplantingswijze sierbeplanting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAanplantingswijzeSierbeplanting'
    definition = 'De mogelijke manieren van aanplanten van sierbeplanting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAanplantingswijzeSierbeplanting'
    options = {
        'aanplanting-bol--en-knolgewassen': KeuzelijstWaarde(invulwaarde='aanplanting-bol--en-knolgewassen',
                                                             label='aanplanting bol- en knolgewassen',
                                                             status='ingebruik',
                                                             definitie='Aanplanting via bol- en knolgewassen',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-bol--en-knolgewassen'),
        'aanplanting-helm': KeuzelijstWaarde(invulwaarde='aanplanting-helm',
                                             label='aanplanting helm',
                                             status='ingebruik',
                                             definitie='Aanplanting via helm',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-helm'),
        'aanplanting-zonder-helm': KeuzelijstWaarde(invulwaarde='aanplanting-zonder-helm',
                                                    label='aanplanting zonder helm',
                                                    status='ingebruik',
                                                    definitie='Aanplanting zonder helm',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAanplantingswijzeSierbeplanting/aanplanting-zonder-helm')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))
