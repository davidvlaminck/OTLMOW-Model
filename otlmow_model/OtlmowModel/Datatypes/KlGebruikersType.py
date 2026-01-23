# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGebruikersType(KeuzelijstField):
    """Geeft weer welke gebruikers op elk element van de koker."""
    naam = 'KlGebruikersType'
    label = 'Koker element gebruikers type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlGebruikersType'
    definition = 'Geeft weer welke gebruikers op elk element van de koker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGebruikersType'
    options = {
        'autosnelweg': KeuzelijstWaarde(invulwaarde='autosnelweg',
                                        label='autosnelweg',
                                        status='verwijderd',
                                        definitie='autosnelweg',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/autosnelweg'),
        'duiker': KeuzelijstWaarde(invulwaarde='duiker',
                                   label='duiker',
                                   status='verwijderd',
                                   definitie='duiker',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/duiker'),
        'ecopassage': KeuzelijstWaarde(invulwaarde='ecopassage',
                                       label='ecopassage',
                                       status='verwijderd',
                                       definitie='ecopassage',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/ecopassage'),
        'geen-gebruikers': KeuzelijstWaarde(invulwaarde='geen-gebruikers',
                                            label='geen gebruikers',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/geen-gebruikers'),
        'hevelduiker': KeuzelijstWaarde(invulwaarde='hevelduiker',
                                        label='hevelduiker',
                                        status='verwijderd',
                                        definitie='hevelduiker',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/hevelduiker'),
        'leiding': KeuzelijstWaarde(invulwaarde='leiding',
                                    label='leiding',
                                    status='verwijderd',
                                    definitie='leiding',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/leiding'),
        'metro': KeuzelijstWaarde(invulwaarde='metro',
                                  label='metro',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/metro'),
        'ruiter': KeuzelijstWaarde(invulwaarde='ruiter',
                                   label='ruiter',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/ruiter'),
        'tram': KeuzelijstWaarde(invulwaarde='tram',
                                 label='tram',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/tram'),
        'trein': KeuzelijstWaarde(invulwaarde='trein',
                                  label='trein',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/trein'),
        'voertuigen': KeuzelijstWaarde(invulwaarde='voertuigen',
                                       label='voertuigen',
                                       status='ingebruik',
                                       definitie='voertuigen (wagens, vrachtwagens,...)',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/voertuigen'),
        'voetgangers-en-of-fietsers': KeuzelijstWaarde(invulwaarde='voetgangers-en-of-fietsers',
                                                       label='voetgangers en of fietsers',
                                                       status='ingebruik',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/voetgangers-en-of-fietsers'),
        'wegverkeer': KeuzelijstWaarde(invulwaarde='wegverkeer',
                                       label='wegverkeer',
                                       status='verwijderd',
                                       definitie='wegverkeer',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/wegverkeer'),
        'wegverkeer-(tern)': KeuzelijstWaarde(invulwaarde='wegverkeer-(tern)',
                                              label='wegverkeer (TERN)',
                                              status='verwijderd',
                                              definitie='wegverkeer (TERN)',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGebruikersType/wegverkeer-(tern)')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

