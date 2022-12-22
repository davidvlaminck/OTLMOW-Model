# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBatterijMateriaal(KeuzelijstField):
    """Keuzelijst voor de verschillende materialen waaruit een batterij gemaakt kan zijn."""
    naam = 'KlBatterijMateriaal'
    label = 'Batterij materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBatterijMateriaal'
    definition = 'Keuzelijst voor de verschillende materialen waaruit een batterij gemaakt kan zijn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBatterijMateriaal'
    options = {
        'lithium-ion-(li-ion)': KeuzelijstWaarde(invulwaarde='lithium-ion-(li-ion)',
                                                 label='Lithium-ion (Li-ion)',
                                                 status='ingebruik',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBatterijMateriaal/lithium-ion-(li-ion)'),
        'loodaccu-(pb)': KeuzelijstWaarde(invulwaarde='loodaccu-(pb)',
                                          label='Loodaccu (Pb)',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBatterijMateriaal/loodaccu-(pb)'),
        'nikkel-cadmium-(nicd)': KeuzelijstWaarde(invulwaarde='nikkel-cadmium-(nicd)',
                                                  label='Nikkel-cadmium (NiCd)',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBatterijMateriaal/nikkel-cadmium-(nicd)'),
        'nikkel-metaalhydride-(nimh)': KeuzelijstWaarde(invulwaarde='nikkel-metaalhydride-(nimh)',
                                                        label='Nikkel-metaalhydride (NiMH)',
                                                        status='ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBatterijMateriaal/nikkel-metaalhydride-(nimh)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

