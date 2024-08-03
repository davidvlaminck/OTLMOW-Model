# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegankelijkheid(KeuzelijstField):
    """De mogelijke opties die de toegankelijkheid van een object aanduiden."""
    naam = 'KlToegankelijkheid'
    label = 'Toegankelijkheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlToegankelijkheid'
    definition = 'De mogelijke opties die de toegankelijkheid van een object aanduiden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegankelijkheid'
    options = {
        'is-bereikbaar-voor-inspectie': KeuzelijstWaarde(invulwaarde='is-bereikbaar-voor-inspectie',
                                                         label='is bereikbaar voor inspectie',
                                                         status='ingebruik',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegankelijkheid/is-bereikbaar-voor-inspectie'),
        'is-betreedbaar': KeuzelijstWaarde(invulwaarde='is-betreedbaar',
                                           label='is betreedbaar',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegankelijkheid/is-betreedbaar'),
        'niet-toegankelijk': KeuzelijstWaarde(invulwaarde='niet-toegankelijk',
                                              label='niet toegankelijk',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegankelijkheid/niet-toegankelijk')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

