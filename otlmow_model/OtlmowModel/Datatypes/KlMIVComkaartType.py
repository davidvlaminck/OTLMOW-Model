# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVComkaartType(KeuzelijstField):
    """Mogelijke opties van Com-kaart types."""
    naam = 'KlMIVComkaartType'
    label = 'MIV comkaart type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMIVComkaartType'
    definition = 'Mogelijke opties van Com-kaart types.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVComkaartType'
    options = {
        '19-inch': KeuzelijstWaarde(invulwaarde='19-inch',
                                    label='19 inch',
                                    status='ingebruik',
                                    definitie='19 inch',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVComkaartType/19-inch'),
        'module': KeuzelijstWaarde(invulwaarde='module',
                                   label='module',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVComkaartType/module'),
        'sat-module': KeuzelijstWaarde(invulwaarde='sat-module',
                                       label='SAT module',
                                       status='ingebruik',
                                       definitie='SAT module',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVComkaartType/sat-module'),
        'serieel': KeuzelijstWaarde(invulwaarde='serieel',
                                    label='serieel',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVComkaartType/serieel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

