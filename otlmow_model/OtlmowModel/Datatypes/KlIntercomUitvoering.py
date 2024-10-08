# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIntercomUitvoering(KeuzelijstField):
    """Keuzelijst met types voor intercomtoestellen naargelang hun functie in het gesloten netwerk"""
    naam = 'KlIntercomUitvoering'
    label = 'Intercom uitvoering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIntercomUitvoering'
    definition = 'Keuzelijst met types voor intercomtoestellen naargelang hun functie in het gesloten netwerk'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIntercomUitvoering'
    options = {
        'antwoordpost': KeuzelijstWaarde(invulwaarde='antwoordpost',
                                         label='antwoordpost',
                                         status='ingebruik',
                                         definitie='Toestel dat bestemd is om in een lokaal netwerk oproepen van een of meer oproepposten te ontvangen.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIntercomUitvoering/antwoordpost'),
        'noodintercom': KeuzelijstWaarde(invulwaarde='noodintercom',
                                         label='noodintercom',
                                         status='ingebruik',
                                         definitie='Oproeppost waarmee een gebruiker rechtstreeks contact opneemt met een noodcentrale. ',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIntercomUitvoering/noodintercom'),
        'oproep-antwoordpost': KeuzelijstWaarde(invulwaarde='oproep-antwoordpost',
                                                label='oproep-antwoordpost',
                                                status='ingebruik',
                                                definitie='Toestel in een netwerk van onderling verbonden toestellen die met elkaar kunnen communiceren.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIntercomUitvoering/oproep-antwoordpost'),
        'oproeppost': KeuzelijstWaarde(invulwaarde='oproeppost',
                                       label='oproeppost',
                                       status='ingebruik',
                                       definitie='Toestel waarmee een gebruiker rechtstreeks een ander toestel binnen een lokaal netwerk kan contacteren of een centrale hoofdpost.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIntercomUitvoering/oproeppost')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

