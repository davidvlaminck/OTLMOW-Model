# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLedLichtkleur(KeuzelijstField):
    """Beschrijving van de kleur van het licht adhv de naam van de kleur."""
    naam = 'KlWvLedLichtkleur'
    label = 'WV LED lichtkleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedLichtkleur'
    definition = 'Beschrijving van de kleur van het licht adhv de naam van de kleur.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedLichtkleur'
    options = {
        'amber': KeuzelijstWaarde(invulwaarde='amber',
                                  label='amber',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/amber'),
        'blauw': KeuzelijstWaarde(invulwaarde='blauw',
                                  label='blauw',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/blauw'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/rood'),
        'wit': KeuzelijstWaarde(invulwaarde='wit',
                                label='wit',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedLichtkleur/wit')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

