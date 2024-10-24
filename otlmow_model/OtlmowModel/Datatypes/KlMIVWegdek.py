# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVWegdek(KeuzelijstField):
    """Het type wegdek waarin de meetlussen zijn verwerkt."""
    naam = 'KlMIVWegdek'
    label = 'MIV wegdek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMIVWegdek'
    definition = 'Het type wegdek waarin de meetlussen zijn verwerkt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVWegdek'
    options = {
        'asfalt': KeuzelijstWaarde(invulwaarde='asfalt',
                                   label='Asfalt',
                                   status='ingebruik',
                                   definitie='Asfalt',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVWegdek/asfalt'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='Beton',
                                  status='ingebruik',
                                  definitie='Beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVWegdek/beton')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

