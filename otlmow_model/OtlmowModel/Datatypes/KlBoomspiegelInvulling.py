# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomspiegelInvulling(KeuzelijstField):
    """Keuzelijst, die de manieren om de boomspiegel in te vullen, oplijst."""
    naam = 'KlBoomspiegelInvulling'
    label = 'Boomspiegel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomspiegelInvulling'
    definition = 'Keuzelijst, die de manieren om de boomspiegel in te vullen, oplijst.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomspiegelInvulling'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   definitie='De boomspiegel bestaat uit ander materiaal dan opgelijst',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/andere'),
        'beplanting': KeuzelijstWaarde(invulwaarde='beplanting',
                                       label='beplanting',
                                       status='ingebruik',
                                       definitie='De boomspiegel bestaat voornamelijk uit sierbeplanting of houtige vegetatie',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/beplanting'),
        'biologisch-afbreekbaar-doek-PLA': KeuzelijstWaarde(invulwaarde='biologisch-afbreekbaar-doek-PLA',
                                                            label='biologisch afbreekbaar doek PLA',
                                                            status='ingebruik',
                                                            definitie='Afdekking van de bodem rond de boom met een biologisch afbreekbaar doek in PLA.',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/biologisch-afbreekbaar-doek-PLA'),
        'biologisch-afbreekbaar-doek-jute': KeuzelijstWaarde(invulwaarde='biologisch-afbreekbaar-doek-jute',
                                                             label='biologisch afbreekbaar doek jute',
                                                             status='ingebruik',
                                                             definitie='Afdekking van de bodem rond de boom met een biologisch afbreekbaar doek in jute.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/biologisch-afbreekbaar-doek-jute'),
        'boomschors': KeuzelijstWaarde(invulwaarde='boomschors',
                                       label='boomschors',
                                       status='ingebruik',
                                       definitie='Afdekking van de bodem rond de boom met boomschors.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/boomschors'),
        'gras': KeuzelijstWaarde(invulwaarde='gras',
                                 label='gras',
                                 status='ingebruik',
                                 definitie='De boomspiegel bestaat voornamelijk uit grazige vegetatie die gemaaid kan worden',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/gras'),
        'groencompost': KeuzelijstWaarde(invulwaarde='groencompost',
                                         label='groencompost',
                                         status='ingebruik',
                                         definitie='Afdekking van de bodem rond de boom met groencompost.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/groencompost'),
        'houtsnippers': KeuzelijstWaarde(invulwaarde='houtsnippers',
                                         label='houtsnippers',
                                         status='ingebruik',
                                         definitie='Afdekking van de bodem rond de boom met houtsnippers.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/houtsnippers'),
        'kaal': KeuzelijstWaarde(invulwaarde='kaal',
                                 label='kaal',
                                 status='ingebruik',
                                 definitie='De boomspiegel is kaal of licht begroeid met onkruid (<25%) en word niet gemaaid',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/kaal'),
        'minerale-mulch': KeuzelijstWaarde(invulwaarde='minerale-mulch',
                                           label='minerale mulch',
                                           status='ingebruik',
                                           definitie='De boomspiegel bestaat uit een bodembedekking van minerale oorsprong (vb. grind, dolomiet)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/minerale-mulch'),
        'organische-mulch': KeuzelijstWaarde(invulwaarde='organische-mulch',
                                             label='organische mulch',
                                             status='ingebruik',
                                             definitie='Afdekking van de bodem rond de boom met organische mulch.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/organische-mulch'),
        'rooster': KeuzelijstWaarde(invulwaarde='rooster',
                                    label='rooster',
                                    status='ingebruik',
                                    definitie='De boomspiegel is een rooster',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/rooster'),
        'verharding': KeuzelijstWaarde(invulwaarde='verharding',
                                       label='verharding',
                                       status='ingebruik',
                                       definitie='In de boomspiegel is verharding aanwezig tot op minder dan 30cm van de stamvoet',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/verharding')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

