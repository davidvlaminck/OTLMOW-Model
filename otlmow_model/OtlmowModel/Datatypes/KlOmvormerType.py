# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmvormerType(KeuzelijstField):
    """De soort omvorming die gebeurt er in de omvormer."""
    naam = 'KlOmvormerType'
    label = 'Omvormer type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmvormerType'
    definition = 'De soort omvorming die gebeurt er in de omvormer.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmvormerType'
    options = {
        'Coax-UTP': KeuzelijstWaarde(invulwaarde='Coax-UTP',
                                     label='Coax-UTP',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Coax-UTP'),
        'Decoder': KeuzelijstWaarde(invulwaarde='Decoder',
                                    label='Decoder',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Decoder'),
        'Encoder': KeuzelijstWaarde(invulwaarde='Encoder',
                                    label='Encoder',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Encoder'),
        'Glasvezel-UTP': KeuzelijstWaarde(invulwaarde='Glasvezel-UTP',
                                          label='Glasvezel-UTP',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Glasvezel-UTP'),
        'UTP-(Serieel)-UTP': KeuzelijstWaarde(invulwaarde='UTP-(Serieel)-UTP',
                                              label='UTP (Serieel)-UTP',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-(Serieel)-UTP'),
        'UTP-Coax': KeuzelijstWaarde(invulwaarde='UTP-Coax',
                                     label='UTP-Coax',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-Coax'),
        'UTP-Glasvezel': KeuzelijstWaarde(invulwaarde='UTP-Glasvezel',
                                          label='UTP-Glasvezel',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-Glasvezel'),
        'UTP-UTP-(serieel)': KeuzelijstWaarde(invulwaarde='UTP-UTP-(serieel)',
                                              label='UTP-UTP (serieel)',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/UTP-UTP-(serieel)'),
        'draadloos-utp': KeuzelijstWaarde(invulwaarde='draadloos-utp',
                                          label='Draadloos-UTP',
                                          status='ingebruik',
                                          definitie='Draadloos-UTP',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/draadloos-utp'),
        'lre': KeuzelijstWaarde(invulwaarde='lre',
                                label='LRE',
                                status='ingebruik',
                                definitie='Long Range Extender voor UTP',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/lre'),
        'rs485-tcp': KeuzelijstWaarde(invulwaarde='rs485-tcp',
                                      label='RS485-TCP',
                                      status='ingebruik',
                                      definitie='Het RS485 signaal wordt omgevormd tot een TCP signaal zodat het over het netwerk kan worden getransporteerd. ',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/rs485-tcp'),
        'utp-draadloos': KeuzelijstWaarde(invulwaarde='utp-draadloos',
                                          label='UTP-Draadloos',
                                          status='ingebruik',
                                          definitie='UTP-Draadloos',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/utp-draadloos')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

