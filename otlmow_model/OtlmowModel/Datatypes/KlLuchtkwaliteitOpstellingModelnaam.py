# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLuchtkwaliteitOpstellingModelnaam(KeuzelijstField):
    """De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie."""
    naam = 'KlLuchtkwaliteitOpstellingModelnaam'
    label = 'Luchtkwaliteitsopstelling modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlLuchtkwaliteitOpstellingModelnaam'
    definition = 'De modelnaam van een onderdeel uit een luchtkwaliteitsinstallatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLuchtkwaliteitOpstellingModelnaam'
    options = {
        'VICOTEC321': KeuzelijstWaarde(invulwaarde='VICOTEC321',
                                       label='VICOTEC321',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuchtkwaliteitOpstellingModelnaam/VICOTEC321'),
        'VICOTEC322': KeuzelijstWaarde(invulwaarde='VICOTEC322',
                                       label='VICOTEC322',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuchtkwaliteitOpstellingModelnaam/VICOTEC322'),
        'VICOTEC323': KeuzelijstWaarde(invulwaarde='VICOTEC323',
                                       label='VICOTEC323',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuchtkwaliteitOpstellingModelnaam/VICOTEC323'),
        'VICOTEC324': KeuzelijstWaarde(invulwaarde='VICOTEC324',
                                       label='VICOTEC324',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuchtkwaliteitOpstellingModelnaam/VICOTEC324')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

