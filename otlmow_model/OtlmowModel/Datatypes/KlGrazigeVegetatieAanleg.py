# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGrazigeVegetatieAanleg(KeuzelijstField):
    """Types van aanleg voor de grazige vegetatie."""
    naam = 'KlGrazigeVegetatieAanleg'
    label = 'Grazige vegetatie aanleg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGrazigeVegetatieAanleg'
    definition = 'Types van aanleg voor de grazige vegetatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGrazigeVegetatieAanleg'
    options = {
        'aanplanting-container-planten': KeuzelijstWaarde(invulwaarde='aanplanting-container-planten',
                                                          label='aanplanting container planten',
                                                          status='ingebruik',
                                                          definitie='Het aanleggen van een grazige vegetatie dmv de aanplant van container planten.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/aanplanting-container-planten'),
        'aanplanting-wortelstokken': KeuzelijstWaarde(invulwaarde='aanplanting-wortelstokken',
                                                      label='aanplanting wortelstokken',
                                                      status='ingebruik',
                                                      definitie='Het aanleggen van een grazige vegetatie dmv de aanplant van wortelstokken.',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/aanplanting-wortelstokken'),
        'bezaaiing': KeuzelijstWaarde(invulwaarde='bezaaiing',
                                      label='bezaaiing',
                                      status='ingebruik',
                                      definitie='Het aanleggen van een grazige vegetatie door het inzaaien van het zaadmengsel.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/bezaaiing'),
        'bezoding': KeuzelijstWaarde(invulwaarde='bezoding',
                                     label='bezoding',
                                     status='ingebruik',
                                     definitie='Het aanleggen van een grazige vegetatie door het naast elkaar leggen van graszoden.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/bezoding'),
        'bloemenmengsel': KeuzelijstWaarde(invulwaarde='bloemenmengsel',
                                           label='bloemenmengsel',
                                           status='ingebruik',
                                           definitie='Het aanleggen van een grazige vegetatie door het inzaaien van een bloemenmengsel.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/bloemenmengsel'),
        'hydraulische-bezaaiing': KeuzelijstWaarde(invulwaarde='hydraulische-bezaaiing',
                                                   label='hydraulische bezaaiing',
                                                   status='ingebruik',
                                                   definitie='Het aanleggen van een grazige vegetatie door het openspreiden van het zaadmengsel met een spuitzaaimachine.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/hydraulische-bezaaiing'),
        'natuurlijke-vegetatie-ontwikkeling-door-behoud-zaadbank': KeuzelijstWaarde(invulwaarde='natuurlijke-vegetatie-ontwikkeling-door-behoud-zaadbank',
                                                                                    label='natuurlijke vegetatie ontwikkeling door behoud zaadbank',
                                                                                    status='ingebruik',
                                                                                    definitie='Het ontstaan van natuurlijke grazige vegetatie door behoud van de zaadbank.',
                                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/natuurlijke-vegetatie-ontwikkeling-door-behoud-zaadbank'),
        'natuurlijke-vegetatie-ontwikkeling-door-overbrengen-maaisel': KeuzelijstWaarde(invulwaarde='natuurlijke-vegetatie-ontwikkeling-door-overbrengen-maaisel',
                                                                                        label='natuurlijke vegetatie ontwikkeling door overbrengen maaisel',
                                                                                        status='ingebruik',
                                                                                        definitie='Het ontstaan van natuurlijke grazige vegetatie door overbrengen van maaisel.',
                                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/natuurlijke-vegetatie-ontwikkeling-door-overbrengen-maaisel'),
        'rhizomen': KeuzelijstWaarde(invulwaarde='rhizomen',
                                     label='rhizomen',
                                     status='ingebruik',
                                     definitie='Het aanleggen van een grazige vegetatie dmv rhizomen.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGrazigeVegetatieAanleg/rhizomen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

