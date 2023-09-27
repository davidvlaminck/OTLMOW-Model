# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDichtingType(KeuzelijstField):
    """Keuzelijst voor de types dichting."""
    naam = 'KlDichtingType'
    label = 'Dichting type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDichtingType'
    definition = 'Keuzelijst voor de types dichting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDichtingType'
    options = {
        'asafdichting': KeuzelijstWaarde(invulwaarde='asafdichting',
                                         label='asafdichting',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDichtingType/asafdichting'),
        'stangafdichting': KeuzelijstWaarde(invulwaarde='stangafdichting',
                                            label='stangafdichting',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDichtingType/stangafdichting'),
        'tandwielkastafdichting': KeuzelijstWaarde(invulwaarde='tandwielkastafdichting',
                                                   label='tandwielkastafdichting',
                                                   status='ingebruik',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDichtingType/tandwielkastafdichting')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

