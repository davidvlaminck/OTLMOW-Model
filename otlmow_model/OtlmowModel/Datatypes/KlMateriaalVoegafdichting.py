# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalVoegafdichting(KeuzelijstField):
    """De lijst met mogelijke materialen waaruit de voegafdichting kan bestaan."""
    naam = 'KlMateriaalVoegafdichting'
    label = 'materiaal voegafdichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalVoegafdichting'
    definition = 'De lijst met mogelijke materialen waaruit de voegafdichting kan bestaan.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalVoegafdichting'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalVoegafdichting/beton'),
        'fpo-flexibele-folyolefine': KeuzelijstWaarde(invulwaarde='fpo-flexibele-folyolefine',
                                                      label='FPO (flexibele folyolefine)',
                                                      status='ingebruik',
                                                      definitie='FPO (flexibele folyolefine)',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalVoegafdichting/fpo-flexibele-folyolefine'),
        'rubber': KeuzelijstWaarde(invulwaarde='rubber',
                                   label='rubber',
                                   status='ingebruik',
                                   definitie='rubber',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalVoegafdichting/rubber'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalVoegafdichting/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

