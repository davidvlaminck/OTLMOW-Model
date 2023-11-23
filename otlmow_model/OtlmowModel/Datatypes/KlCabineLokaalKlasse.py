# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCabineLokaalKlasse(KeuzelijstField):
    """Lijst van waarden voor de classificatie van de hoogspanningscabine als lokaal volgens Synergrid."""
    naam = 'KlCabineLokaalKlasse'
    label = 'Cabine lokaal klasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineLokaalKlasse'
    definition = 'Lijst van waarden voor de classificatie van de hoogspanningscabine als lokaal volgens Synergrid.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineLokaalKlasse'
    options = {
        'BB00': KeuzelijstWaarde(invulwaarde='BB00',
                                 label='BB00',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB00'),
        'BB05': KeuzelijstWaarde(invulwaarde='BB05',
                                 label='BB05',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB05'),
        'BB10': KeuzelijstWaarde(invulwaarde='BB10',
                                 label='BB10',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB10'),
        'BB20': KeuzelijstWaarde(invulwaarde='BB20',
                                 label='BB20',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB20'),
        'BB30': KeuzelijstWaarde(invulwaarde='BB30',
                                 label='BB30',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB30'),
        'BB40': KeuzelijstWaarde(invulwaarde='BB40',
                                 label='BB40',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB40'),
        'BB50': KeuzelijstWaarde(invulwaarde='BB50',
                                 label='BB50',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineLokaalKlasse/BB50')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

