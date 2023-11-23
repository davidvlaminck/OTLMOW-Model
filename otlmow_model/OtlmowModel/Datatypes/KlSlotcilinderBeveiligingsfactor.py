# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlotcilinderBeveiligingsfactor(KeuzelijstField):
    """Keuzelijst voor de beveiligingsfactor van de slotcilinder."""
    naam = 'KlSlotcilinderBeveiligingsfactor'
    label = 'Slotcilinder beveiligingsfactor'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlotcilinderBeveiligingsfactor'
    definition = 'Keuzelijst voor de beveiligingsfactor van de slotcilinder.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlotcilinderBeveiligingsfactor'
    options = {
        'skg-1-ster': KeuzelijstWaarde(invulwaarde='skg-1-ster',
                                       label='SKG 1 ster',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotcilinderBeveiligingsfactor/skg-1-ster'),
        'skg-2-sterren': KeuzelijstWaarde(invulwaarde='skg-2-sterren',
                                          label='SKG 2 sterren',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotcilinderBeveiligingsfactor/skg-2-sterren'),
        'skg-3-sterren': KeuzelijstWaarde(invulwaarde='skg-3-sterren',
                                          label='SKG 3 sterren',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotcilinderBeveiligingsfactor/skg-3-sterren')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

