# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGroutankerInjectie(KeuzelijstField):
    """Manier waarop het groutanker wordt uitgevoerd."""
    naam = 'KlGroutankerInjectie'
    label = 'groutanker injectie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGroutankerInjectie'
    definition = 'Manier waarop het groutanker wordt uitgevoerd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGroutankerInjectie'
    options = {
        'igu-(injection-globale-et-unitaire)': KeuzelijstWaarde(invulwaarde='igu-(injection-globale-et-unitaire)',
                                                                label='IGU (Injection Globale et Unitaire)',
                                                                status='ingebruik',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroutankerInjectie/igu-(injection-globale-et-unitaire)'),
        'irs-(injection-repetitive-et-selective)': KeuzelijstWaarde(invulwaarde='irs-(injection-repetitive-et-selective)',
                                                                    label='IRS (Injection Répétitive et Sélective)',
                                                                    status='ingebruik',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroutankerInjectie/irs-(injection-repetitive-et-selective)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

