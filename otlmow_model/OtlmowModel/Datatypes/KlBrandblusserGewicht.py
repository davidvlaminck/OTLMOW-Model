# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBrandblusserGewicht(KeuzelijstField):
    """Keuzelijst met de mogelijke gewichten van brandblussers."""
    naam = 'KlBrandblusserGewicht'
    label = 'Brandblusser gewicht'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBrandblusserGewicht'
    definition = 'Keuzelijst met de mogelijke gewichten van brandblussers.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBrandblusserGewicht'
    options = {
        '6-kg': KeuzelijstWaarde(invulwaarde='6-kg',
                                 label='6 kg',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserGewicht/6-kg'),
        '9-kg': KeuzelijstWaarde(invulwaarde='9-kg',
                                 label='9 kg',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBrandblusserGewicht/9-kg')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

