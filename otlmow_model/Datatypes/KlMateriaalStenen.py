# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalStenen(KeuzelijstField):
    """Het materiaal van de stenen."""
    naam = 'KlMateriaalStenen'
    label = 'Materiaal stenen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalStenen'
    definition = 'Het materiaal van de stenen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalStenen'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='Beton',
                                  status='ingebruik',
                                  definitie='Betonspecie van zand, cement, grind, water en eventueel vulstoffen en hulpstoffen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/beton'),
        'blauwe-hardsteen-volgens-categorie-a': KeuzelijstWaarde(invulwaarde='blauwe-hardsteen-volgens-categorie-a',
                                                                 label='Blauwe hardsteen volgens categorie A',
                                                                 status='ingebruik',
                                                                 definitie='Ook wel: Petit Granit. Een natuursteen met een natuurlijke blauwgrijze kleur door de aanwezigheid van crinoÃ¯deresten samengeklit met microkristallijn calciet. Blauwe hardsteen van categorie A wordt gebruikt in beeldhouwwerken, grafzerken of werken met een uitzonderlijke afwerking.',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/blauwe-hardsteen-volgens-categorie-a'),
        'blauwe-hardsteen-volgens-categorie-b': KeuzelijstWaarde(invulwaarde='blauwe-hardsteen-volgens-categorie-b',
                                                                 label='Blauwe hardsteen volgens categorie B',
                                                                 status='ingebruik',
                                                                 definitie='Ook wel: Petit Granit. Een natuursteen met een natuurlijke blauwgrijze kleur door de aanwezigheid van crinoÃ¯deresten samengeklit met microkristallijn calciet. Blauwe hardsteen van categorie B wordt gebruikt in bouwwerken, restauratiewerken of marmerwerken.',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/blauwe-hardsteen-volgens-categorie-b'),
        'blauwe-hardsteen-volgens-categorie-c': KeuzelijstWaarde(invulwaarde='blauwe-hardsteen-volgens-categorie-c',
                                                                 label='Blauwe hardsteen volgens categorie C',
                                                                 status='ingebruik',
                                                                 definitie='Ook wel: Petit Granit. Een natuursteen met een natuurlijke blauwgrijze kleur door de aanwezigheid van crinoÃ¯deresten samengeklit met microkristallijn calciet. Blauwe hardsteen van categorie C wordt gebruikt in houwstenen of bekledingswerken.',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/blauwe-hardsteen-volgens-categorie-c'),
        'breuksteen': KeuzelijstWaarde(invulwaarde='breuksteen',
                                       label='Breuksteen',
                                       status='ingebruik',
                                       definitie='Breuksteen is een natuursteen van onregelmatige vorm.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/breuksteen'),
        'cellenbeton': KeuzelijstWaarde(invulwaarde='cellenbeton',
                                        label='Cellenbeton',
                                        status='ingebruik',
                                        definitie='Ook wel: gasbeton. Dit is een betonsoort die gekenmerkt wordt door zijn lage dichtheid en sterk isolerend vermogen. Het bekendste merk is Ytong.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/cellenbeton'),
        'crino-denkalksteen': KeuzelijstWaarde(invulwaarde='crino-denkalksteen',
                                               label='Crinoïdenkalksteen',
                                               status='ingebruik',
                                               definitie='Kalksteen met vele overblijfselen, voornamelijk stengeldelen, van Crinoiden of Haarsterren.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/crino-denkalksteen'),
        'gevelsteen': KeuzelijstWaarde(invulwaarde='gevelsteen',
                                       label='Gevelsteen',
                                       status='ingebruik',
                                       definitie='Een gevelsteen is een baksteen die toegepast kan worden als buitengevelsteen.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/gevelsteen'),
        'kalksteen': KeuzelijstWaarde(invulwaarde='kalksteen',
                                      label='Kalksteen',
                                      status='ingebruik',
                                      definitie='Een natuursteen, ontstaan door kalkafzettingen.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/kalksteen'),
        'leisteen': KeuzelijstWaarde(invulwaarde='leisteen',
                                     label='Leisteen',
                                     status='ingebruik',
                                     definitie='Een metamorf gesteente dat gekenmerkt is door een duidelijke foliatie van afwisselende laagjes kwarts en andere mineralen.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/leisteen'),
        'natuursteen': KeuzelijstWaarde(invulwaarde='natuursteen',
                                        label='Natuursteen',
                                        status='ingebruik',
                                        definitie='Een gesteente dat in de natuur wordt aangetroffen en dat, na een eventuele bewerking, geschikt is als bouwmateriaal.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/natuursteen'),
        'snelbouwsteen': KeuzelijstWaarde(invulwaarde='snelbouwsteen',
                                          label='Snelbouwsteen',
                                          status='ingebruik',
                                          definitie='Dit is een keramische binnenmuursteen die vooral uit klei(houdende) materialen bestaat, al dan niet gemengd met zand en andere toeslagstoffen.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/snelbouwsteen'),
        'volle-baksteen': KeuzelijstWaarde(invulwaarde='volle-baksteen',
                                           label='Volle baksteen',
                                           status='ingebruik',
                                           definitie='Aarde die in een bepaald vorm gebakken wordt.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/volle-baksteen'),
        'zandsteen': KeuzelijstWaarde(invulwaarde='zandsteen',
                                      label='Zandsteen',
                                      status='ingebruik',
                                      definitie='Een afzettingsgesteente dat voornamelijk bestaat uit zand/kwartskorrels die met elkaar verbonden werden met een bindmiddel (leem, kalk,...).',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalStenen/zandsteen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

