# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBijlageType(KeuzelijstField):
    """De mogelijke types of categorieën van het document."""
    naam = 'KlBijlageType'
    label = 'Bijlage type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlBijlageType'
    definition = 'De mogelijke types of categorieën van het document.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBijlageType'
    options = {
        'foto': KeuzelijstWaarde(invulwaarde='foto',
                                 label='foto',
                                 status='ingebruik',
                                 definitie='foto',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageType/foto')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

