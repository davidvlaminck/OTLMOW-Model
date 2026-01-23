# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRelaisMerk(KeuzelijstField):
    """Lijst met merknamen voor relais volgens de fabrikant."""
    naam = 'KlRelaisMerk'
    label = 'Merken relais'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRelaisMerk'
    definition = 'Lijst met merknamen voor relais volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRelaisMerk'
    options = {
        'crouzet': KeuzelijstWaarde(invulwaarde='crouzet',
                                    label='Crouzet',
                                    status='ingebruik',
                                    definitie='Crouzet',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRelaisMerk/crouzet'),
        'schneider': KeuzelijstWaarde(invulwaarde='schneider',
                                      label='Schneider',
                                      status='ingebruik',
                                      definitie='Schneider',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRelaisMerk/schneider'),
        'tele-haase': KeuzelijstWaarde(invulwaarde='tele-haase',
                                       label='Tele Haase',
                                       status='ingebruik',
                                       definitie='Tele Haase',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRelaisMerk/tele-haase'),
        'wei': KeuzelijstWaarde(invulwaarde='wei',
                                label='WEI',
                                status='ingebruik',
                                definitie='WEI',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRelaisMerk/wei')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

