# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStortsteenpenetratieMateriaal(KeuzelijstField):
    """Het materiaal met welk de stortstenen worden gepenetreerd."""
    naam = 'KlStortsteenpenetratieMateriaal'
    label = 'Stortsteenpenetratiemateriaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStortsteenpenetratieMateriaal'
    definition = 'Het materiaal met welk de stortstenen worden gepenetreerd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStortsteenpenetratieMateriaal'
    options = {
        'asfalt': KeuzelijstWaarde(invulwaarde='asfalt',
                                   label='asfalt',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenpenetratieMateriaal/asfalt'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenpenetratieMateriaal/beton')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

