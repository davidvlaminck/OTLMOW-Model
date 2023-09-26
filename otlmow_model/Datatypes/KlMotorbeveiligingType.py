# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMotorbeveiligingType(KeuzelijstField):
    """Types voor toestellen voor motorbeveiliging volgens de toegepaste techniek."""
    naam = 'KlMotorbeveiligingType'
    label = 'Motorbeveiliging type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMotorbeveiligingType'
    definition = 'Types voor toestellen voor motorbeveiliging volgens de toegepaste techniek.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMotorbeveiligingType'
    options = {
        'koppelcontrole': KeuzelijstWaarde(invulwaarde='koppelcontrole',
                                           label='koppelcontrole',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMotorbeveiligingType/koppelcontrole'),
        'magnetisch': KeuzelijstWaarde(invulwaarde='magnetisch',
                                       label='magnetisch',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMotorbeveiligingType/magnetisch'),
        'thermisch': KeuzelijstWaarde(invulwaarde='thermisch',
                                      label='thermisch',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMotorbeveiligingType/thermisch')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

