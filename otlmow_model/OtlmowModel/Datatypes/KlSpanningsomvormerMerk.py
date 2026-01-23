# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSpanningsomvormerMerk(KeuzelijstField):
    """Lijst van merknamen van spanningsomvormers volgens de fabrikant."""
    naam = 'KlSpanningsomvormerMerk'
    label = 'Merknamen spanningsomvormers'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSpanningsomvormerMerk'
    definition = 'Lijst van merknamen van spanningsomvormers volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSpanningsomvormerMerk'
    options = {
        'eltek': KeuzelijstWaarde(invulwaarde='eltek',
                                  label='Eltek',
                                  status='ingebruik',
                                  definitie='Eltek',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerMerk/eltek'),
        'phoenix-contact': KeuzelijstWaarde(invulwaarde='phoenix-contact',
                                            label='Phoenix Contact',
                                            status='ingebruik',
                                            definitie='Phoenix Contact',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerMerk/phoenix-contact'),
        'puls': KeuzelijstWaarde(invulwaarde='puls',
                                 label='Puls',
                                 status='ingebruik',
                                 definitie='Puls',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSpanningsomvormerMerk/puls')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

