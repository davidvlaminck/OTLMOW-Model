# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWaterloopCategorie(KeuzelijstField):
    """De verschillende categorieën van een waterloop."""
    naam = 'KlWaterloopCategorie'
    label = 'Waterloop categorieën'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlWaterloopCategorie'
    definition = 'De verschillende categorieën van een waterloop.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWaterloopCategorie'
    options = {
        'onbevaarbaar-cat1': KeuzelijstWaarde(invulwaarde='onbevaarbaar-cat1',
                                              label='Onbevaarbaar cat1',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWaterloopCategorie/onbevaarbaar-cat1'),
        'onbevaarbaar-cat2': KeuzelijstWaarde(invulwaarde='onbevaarbaar-cat2',
                                              label='Onbevaarbaar cat2',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWaterloopCategorie/onbevaarbaar-cat2'),
        'onbevaarbaar-cat3': KeuzelijstWaarde(invulwaarde='onbevaarbaar-cat3',
                                              label='Onbevaarbaar cat3',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWaterloopCategorie/onbevaarbaar-cat3')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

