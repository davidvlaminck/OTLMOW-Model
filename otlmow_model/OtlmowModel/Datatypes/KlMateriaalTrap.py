# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalTrap(KeuzelijstField):
    """De keuzelijst die de verschillende mogelijke materialen voor een trap bevat."""
    naam = 'KlMateriaalTrap'
    label = 'keuzelijst materialen trap'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalTrap'
    definition = 'De keuzelijst die de verschillende mogelijke materialen voor een trap bevat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalTrap'
    options = {
        'aluminium': KeuzelijstWaarde(invulwaarde='aluminium',
                                      label='aluminium',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTrap/aluminium'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTrap/beton'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTrap/kunststof'),
        'natuursteen': KeuzelijstWaarde(invulwaarde='natuursteen',
                                        label='natuursteen',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTrap/natuursteen'),
        'roestvrijstaal': KeuzelijstWaarde(invulwaarde='roestvrijstaal',
                                           label='roestvrijstaal',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTrap/roestvrijstaal'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTrap/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

