# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalDeklaag(KeuzelijstField):
    """Lijst van mogelijke materialen voor de deklaag."""
    naam = 'KlMateriaalDeklaag'
    label = 'Materiaal deklaag'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalDeklaag'
    definition = 'Lijst van mogelijke materialen voor de deklaag.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalDeklaag'
    options = {
        'composiet': KeuzelijstWaarde(invulwaarde='composiet',
                                      label='composiet',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDeklaag/composiet'),
        'keramische-laag': KeuzelijstWaarde(invulwaarde='keramische-laag',
                                            label='keramische laag',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDeklaag/keramische-laag'),
        'nvt': KeuzelijstWaarde(invulwaarde='nvt',
                                label='nvt',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDeklaag/nvt'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='rvs',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalDeklaag/rvs')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

