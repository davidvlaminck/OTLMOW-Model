# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZelfsluiterUitvoeringswijze(KeuzelijstField):
    """Lijst met mogelijke uitvoeringen van zelfsluiters voor deuren, poorten etc."""
    naam = 'KlZelfsluiterUitvoeringswijze'
    label = 'Zelfsluiter uitvoeringswijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlZelfsluiterUitvoeringswijze'
    definition = 'Lijst met mogelijke uitvoeringen van zelfsluiters voor deuren, poorten etc.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZelfsluiterUitvoeringswijze'
    options = {
        'met-open-stand': KeuzelijstWaarde(invulwaarde='met-open-stand',
                                           label='met open stand',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZelfsluiterUitvoeringswijze/met-open-stand'),
        'standaard': KeuzelijstWaarde(invulwaarde='standaard',
                                      label='standaard',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZelfsluiterUitvoeringswijze/standaard')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

