# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACTypeEindstuk(KeuzelijstField):
    """De verschillende types eindstukken."""
    naam = 'KlLEACTypeEindstuk'
    label = 'Type eindstuk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACTypeEindstuk'
    definition = 'De verschillende types eindstukken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACTypeEindstuk'
    options = {
        'naar-beneden-afgebogen': KeuzelijstWaarde(invulwaarde='naar-beneden-afgebogen',
                                                   label='naar beneden afgebogen',
                                                   status='ingebruik',
                                                   definitie='naar beneden afgebogen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/naar-beneden-afgebogen'),
        'schelp': KeuzelijstWaarde(invulwaarde='schelp',
                                   label='schelp',
                                   status='ingebruik',
                                   definitie='schelp',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/schelp'),
        'uitgebogen': KeuzelijstWaarde(invulwaarde='uitgebogen',
                                       label='uitgebogen',
                                       status='ingebruik',
                                       definitie='uitgebogen',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACTypeEindstuk/uitgebogen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

