# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStalenDamplankvorm(KeuzelijstField):
    """De vorm van de stalen damplank."""
    naam = 'KlStalenDamplankvorm'
    label = 'Stalen damplankvorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStalenDamplankvorm'
    definition = 'De vorm van de stalen damplank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStalenDamplankvorm'
    options = {
        'plat': KeuzelijstWaarde(invulwaarde='plat',
                                 label='plat',
                                 status='ingebruik',
                                 definitie='plat',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStalenDamplankvorm/plat'),
        'u-profiel': KeuzelijstWaarde(invulwaarde='u-profiel',
                                      label='u-profiel',
                                      status='ingebruik',
                                      definitie='u-profiel',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStalenDamplankvorm/u-profiel'),
        'z-profiel': KeuzelijstWaarde(invulwaarde='z-profiel',
                                      label='z-profiel',
                                      status='ingebruik',
                                      definitie='z-profiel',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStalenDamplankvorm/z-profiel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

