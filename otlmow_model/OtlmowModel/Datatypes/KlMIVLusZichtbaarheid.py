# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVLusZichtbaarheid(KeuzelijstField):
    """Is de lus zichtbaar in het wegdek of bedenkt door een toplaag."""
    naam = 'KlMIVLusZichtbaarheid'
    label = 'MIV-lus zichtbaarheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMIVLusZichtbaarheid'
    definition = 'Is de lus zichtbaar in het wegdek of bedenkt door een toplaag.'
    status = 'ingebruik'
    deprecated_version = '2.9.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVLusZichtbaarheid'
    options = {
        'onderlaag': KeuzelijstWaarde(invulwaarde='onderlaag',
                                      label='onderlaag',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusZichtbaarheid/onderlaag'),
        'toplaag': KeuzelijstWaarde(invulwaarde='toplaag',
                                    label='toplaag',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVLusZichtbaarheid/toplaag')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

