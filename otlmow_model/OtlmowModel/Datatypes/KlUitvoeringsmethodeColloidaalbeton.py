# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitvoeringsmethodeColloidaalbeton(KeuzelijstField):
    """De mogelijke uitvoeringsmethoden van colloïdaal beton."""
    naam = 'KlUitvoeringsmethodeColloidaalbeton'
    label = 'Uitvoeringsmethode colloïdaal beton'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlUitvoeringsmethodeColloidaalbeton'
    definition = 'De mogelijke uitvoeringsmethoden van colloïdaal beton.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitvoeringsmethodeColloidaalbeton'
    options = {
        'hop-dobber': KeuzelijstWaarde(invulwaarde='hop-dobber',
                                       label='hop-dobber',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethodeColloidaalbeton/hop-dobber'),
        'venturi': KeuzelijstWaarde(invulwaarde='venturi',
                                    label='venturi',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethodeColloidaalbeton/venturi')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

