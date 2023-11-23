# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignalisatieReferentiepuntType(KeuzelijstField):
    """Een keuzelijst om het referentiepunt type te bepalen."""
    naam = 'KlSignalisatieReferentiepuntType'
    label = 'Signalisatie referentiepunt type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignalisatieReferentiepuntType'
    definition = 'Een keuzelijst om het referentiepunt type te bepalen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignalisatieReferentiepuntType'
    options = {
        'hectometerpalen-in-kunststof': KeuzelijstWaarde(invulwaarde='hectometerpalen-in-kunststof',
                                                         label='hectometerpalen in kunststof',
                                                         status='ingebruik',
                                                         definitie='Een kleine paal in kunststof die op elke 100 meter langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/hectometerpalen-in-kunststof'),
        'hectometerpunt-aan-ronde-steun': KeuzelijstWaarde(invulwaarde='hectometerpunt-aan-ronde-steun',
                                                           label='hectometerpunt aan ronde steun',
                                                           status='ingebruik',
                                                           definitie='Een hectometerbord bevestigd aan een ronde steun die op elke 100 meter langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/hectometerpunt-aan-ronde-steun'),
        'hectometerpunt-op-horizontale-wand': KeuzelijstWaarde(invulwaarde='hectometerpunt-op-horizontale-wand',
                                                               label='hectometerpunt op horizontale wand',
                                                               status='ingebruik',
                                                               definitie='Een hectometerbord bevestigd tegen een horizontale wand (zoals bv een New Jersey) die op elke 100 meter langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/hectometerpunt-op-horizontale-wand'),
        'kilometerpalen-in-kunststof': KeuzelijstWaarde(invulwaarde='kilometerpalen-in-kunststof',
                                                        label='kilometerpalen in kunststof',
                                                        status='ingebruik',
                                                        definitie='Een kleine paal in kunststof die op elke kilometer langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/kilometerpalen-in-kunststof'),
        'kilometerpunt-aan-ronde-steun': KeuzelijstWaarde(invulwaarde='kilometerpunt-aan-ronde-steun',
                                                          label='kilometerpunt aan ronde steun',
                                                          status='ingebruik',
                                                          definitie='Een kilometerbord bevestigd aan een ronde steun die op elke kilometer langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/kilometerpunt-aan-ronde-steun'),
        'kilometerpunt-op-horizontale-wand': KeuzelijstWaarde(invulwaarde='kilometerpunt-op-horizontale-wand',
                                                              label='kilometerpunt op horizontale wand',
                                                              status='ingebruik',
                                                              definitie='Een kilometerbord bevestigd tegen een horizontale wand (zoals bv een New Jersey) die op elke kilometer langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/kilometerpunt-op-horizontale-wand')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

