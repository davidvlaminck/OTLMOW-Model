# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSluisCategorie(KeuzelijstField):
    """De mogelijke categorieën van een sluis."""
    naam = 'KlSluisCategorie'
    label = 'Sluiscategorie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSluisCategorie'
    definition = 'De mogelijke categorieën van een sluis.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSluisCategorie'
    options = {
        'binnenvaartsluis': KeuzelijstWaarde(invulwaarde='binnenvaartsluis',
                                             label='binnenvaartsluis',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSluisCategorie/binnenvaartsluis'),
        'getijdesluis': KeuzelijstWaarde(invulwaarde='getijdesluis',
                                         label='getijdesluis',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSluisCategorie/getijdesluis'),
        'stuwsluis': KeuzelijstWaarde(invulwaarde='stuwsluis',
                                      label='stuwsluis',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSluisCategorie/stuwsluis'),
        'zeesluis': KeuzelijstWaarde(invulwaarde='zeesluis',
                                     label='zeesluis',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSluisCategorie/zeesluis')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

