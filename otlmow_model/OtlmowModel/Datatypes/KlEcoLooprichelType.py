# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoLooprichelType(KeuzelijstField):
    """Types van looprichel."""
    naam = 'KlEcoLooprichelType'
    label = 'Looprichel type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoLooprichelType'
    definition = 'Types van looprichel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoLooprichelType'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  definitie='Een betonnen looprichel.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/beton'),
        'doorlopende-natuurlijke-oever': KeuzelijstWaarde(invulwaarde='doorlopende-natuurlijke-oever',
                                                          label='doorlopende natuurlijke oever',
                                                          status='ingebruik',
                                                          definitie='Een doorlopende natuurlijke oever.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/doorlopende-natuurlijke-oever'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 definitie='Een houten looprichel.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/hout'),
        'schanskorven': KeuzelijstWaarde(invulwaarde='schanskorven',
                                         label='schanskorven',
                                         status='ingebruik',
                                         definitie='Een oever bestaande uit schanskorven.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoLooprichelType/schanskorven')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

