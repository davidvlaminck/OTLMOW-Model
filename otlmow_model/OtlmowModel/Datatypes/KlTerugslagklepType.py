# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTerugslagklepType(KeuzelijstField):
    """Keuzelijst voor het bepalen van Types van terugslagklep."""
    naam = 'KlTerugslagklepType'
    label = 'Terugslagklep type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTerugslagklepType'
    definition = 'Keuzelijst voor het bepalen van Types van terugslagklep.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTerugslagklepType'
    options = {
        'balkeerklep': KeuzelijstWaarde(invulwaarde='balkeerklep',
                                        label='balkeerklep',
                                        status='ingebruik',
                                        definitie='balkeerklep',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTerugslagklepType/balkeerklep'),
        'scharnierend': KeuzelijstWaarde(invulwaarde='scharnierend',
                                         label='scharnierend',
                                         status='ingebruik',
                                         definitie='Klep bevestigd aan een scharnier, bedoeld om terugstroom in het stelsel vanuit het oppervlaktewater te voorkomen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTerugslagklepType/scharnierend'),
        'vorm-eendebek': KeuzelijstWaarde(invulwaarde='vorm-eendebek',
                                          label='vorm eendebek',
                                          status='ingebruik',
                                          definitie='Eendebek, bedoeld om terugstroom in het stelsel vanuit het oppervlaktewater te voorkomen',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTerugslagklepType/vorm-eendebek')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

