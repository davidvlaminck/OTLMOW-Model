# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoBoombrugType(KeuzelijstField):
    """Types van boombrug."""
    naam = 'KlEcoBoombrugType'
    label = 'Boombrug type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoBoombrugType'
    definition = 'Types van boombrug.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoBoombrugType'
    options = {
        'ladderbrug': KeuzelijstWaarde(invulwaarde='ladderbrug',
                                       label='ladderbrug',
                                       status='ingebruik',
                                       definitie='Een boombrug waarbij de oversteek bestaat uit een laddervorm gemaakt uit touw (touwladder) of metaal-kunststof (kabelnet) of een weefsel van takken en nylon (Takkenmat).',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoBoombrugType/ladderbrug'),
        'portaal-boomgoot': KeuzelijstWaarde(invulwaarde='portaal-boomgoot',
                                             label='portaal boomgoot',
                                             status='ingebruik',
                                             definitie='Een bestaande portaal voor signalisatie ingericht als boomrug door middel van een aluminium ladder of houten loopplank of goot.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoBoombrugType/portaal-boomgoot'),
        'touwbrug': KeuzelijstWaarde(invulwaarde='touwbrug',
                                     label='touwbrug',
                                     status='ingebruik',
                                     definitie='Een boombrug bestaande uit een gedraaid touw van natuurlijke of kunstmatige vezels, dat strak over de weg wordt gespannen en voldoende dik is om er dieren op een stabiele wijze overheen te laten lopen.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoBoombrugType/touwbrug'),
        'tunnelbrug': KeuzelijstWaarde(invulwaarde='tunnelbrug',
                                       label='tunnelbrug',
                                       status='ingebruik',
                                       definitie='Een boombrug bestaande uit een tunnelvormige oversteek gemaakt uit geweven touwen (touwtunnel) of een buisvormige draadkoker (kokerbrug)',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoBoombrugType/tunnelbrug')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

