# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelLeidingBescherming(KeuzelijstField):
    """Lijst met mogelijke types bijkomende mechanische bescherming van kabels of leidingen."""
    naam = 'KlKabelLeidingBescherming'
    label = 'Kabels en Leidingen bescherming'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelLeidingBescherming'
    definition = 'Lijst met mogelijke types bijkomende mechanische bescherming van kabels of leidingen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelLeidingBescherming'
    options = {
        'kabeldekband': KeuzelijstWaarde(invulwaarde='kabeldekband',
                                         label='kabeldekband',
                                         status='ingebruik',
                                         definitie='Bescherming van kabels en leidingen in de vorm van een band (uitgevoerd in hoogwaardig hogedrukpolyethyleen).',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/kabeldekband'),
        'mager-beton': KeuzelijstWaarde(invulwaarde='mager-beton',
                                        label='mager beton',
                                        status='ingebruik',
                                        definitie='Bescherming voor kabels of leidingen in mager beton.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/mager-beton'),
        'niet-gekend': KeuzelijstWaarde(invulwaarde='niet-gekend',
                                        label='niet gekend',
                                        status='ingebruik',
                                        definitie='Het type bescherming kan niet langer achterhaald worden zonder bijzondere inventarisatie inspanningen of zal in een latere fase toegevoegd worden.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/niet-gekend'),
        'omegaprofiel': KeuzelijstWaarde(invulwaarde='omegaprofiel',
                                         label='omegaprofiel',
                                         status='ingebruik',
                                         definitie='Bescherming van kabels of leidingen door middel van een omegaprofiel.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/omegaprofiel'),
        'synthetische-kabeldekking': KeuzelijstWaarde(invulwaarde='synthetische-kabeldekking',
                                                      label='synthetische kabeldekking',
                                                      status='ingebruik',
                                                      definitie='Bescherming van kabels en leidingen door middel van een synthetische kabeldekking.',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/synthetische-kabeldekking'),
        'tegels': KeuzelijstWaarde(invulwaarde='tegels',
                                   label='tegels',
                                   status='ingebruik',
                                   definitie='Bescherming van kabels of leidingen door middel van tegels.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/tegels'),
        'u-ijzers': KeuzelijstWaarde(invulwaarde='u-ijzers',
                                     label='u-ijzers',
                                     status='ingebruik',
                                     definitie='Bescherming van kabels en leidingen door middel van metaal dekkingen in de vorm van een u die boven de kabels of leidingen geplaatst worden.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/u-ijzers'),
        'waarschuwingslint': KeuzelijstWaarde(invulwaarde='waarschuwingslint',
                                              label='waarschuwingslint',
                                              status='ingebruik',
                                              definitie='Bescherming tegen beschadiging van kabels of leidingen door middel van een lint dat wijst op de aanwezigheid van kabels of leidingen in de onmiddellijke nabijheid.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/waarschuwingslint'),
        'waarschuwingsnet': KeuzelijstWaarde(invulwaarde='waarschuwingsnet',
                                             label='waarschuwingsnet',
                                             status='ingebruik',
                                             definitie='Bescherming tegen beschadiging van kabels en leidingen door middel van een net dat waarschuwt voor de aanwezigheid van kabels en leidingen in de onmiddellijke nabijheid.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelLeidingBescherming/waarschuwingsnet')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

