# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkconfiguratieWV(KeuzelijstField):
    """De mogelijke opties van de netwerkconfiguratie in het kader van de gesplitste netwerkenopstelling van de lichtpuntcontrole inzake wegverlichting."""
    naam = 'KlNetwerkconfiguratieWV'
    label = 'Netwerkconfiguratie wegverlichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkconfiguratieWV'
    definition = 'De mogelijke opties van de netwerkconfiguratie in het kader van de gesplitste netwerkenopstelling van de lichtpuntcontrole inzake wegverlichting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkconfiguratieWV'
    options = {
        'black': KeuzelijstWaarde(invulwaarde='black',
                                  label='Black',
                                  status='ingebruik',
                                  definitie='Black',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkconfiguratieWV/black'),
        'blue': KeuzelijstWaarde(invulwaarde='blue',
                                 label='Blue',
                                 status='ingebruik',
                                 definitie='Blue',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkconfiguratieWV/blue'),
        'cyan': KeuzelijstWaarde(invulwaarde='cyan',
                                 label='Cyan',
                                 status='ingebruik',
                                 definitie='Cyan',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkconfiguratieWV/cyan'),
        'green': KeuzelijstWaarde(invulwaarde='green',
                                  label='Green',
                                  status='ingebruik',
                                  definitie='Green',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkconfiguratieWV/green'),
        'kleurloos': KeuzelijstWaarde(invulwaarde='kleurloos',
                                      label='Kleurloos',
                                      status='ingebruik',
                                      definitie='Kleurloos',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkconfiguratieWV/kleurloos'),
        'magenta': KeuzelijstWaarde(invulwaarde='magenta',
                                    label='Magenta',
                                    status='ingebruik',
                                    definitie='Magenta',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkconfiguratieWV/magenta'),
        'red': KeuzelijstWaarde(invulwaarde='red',
                                label='Red',
                                status='ingebruik',
                                definitie='Red',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkconfiguratieWV/red'),
        'yellow': KeuzelijstWaarde(invulwaarde='yellow',
                                   label='Yellow',
                                   status='ingebruik',
                                   definitie='Yellow',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkconfiguratieWV/yellow')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

