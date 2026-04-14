# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKunststoffenDamplankvorm(KeuzelijstField):
    """De vorm van de kunststoffen damplank."""
    naam = 'KlKunststoffenDamplankvorm'
    label = 'Kunststoffen damplankvorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKunststoffenDamplankvorm'
    definition = 'De vorm van de kunststoffen damplank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKunststoffenDamplankvorm'
    options = {
        'fp-profiel': KeuzelijstWaarde(invulwaarde='fp-profiel',
                                       label='FP-profiel',
                                       status='ingebruik',
                                       definitie='fp-profiel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKunststoffenDamplankvorm/fp-profiel'),
        'omega-profiel': KeuzelijstWaarde(invulwaarde='omega-profiel',
                                          label='omega-profiel',
                                          status='ingebruik',
                                          definitie='omega-profiel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKunststoffenDamplankvorm/omega-profiel'),
        'plat': KeuzelijstWaarde(invulwaarde='plat',
                                 label='plat',
                                 status='ingebruik',
                                 definitie='plat',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKunststoffenDamplankvorm/plat'),
        'u-profiel': KeuzelijstWaarde(invulwaarde='u-profiel',
                                      label='u-profiel',
                                      status='ingebruik',
                                      definitie='u-profiel',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKunststoffenDamplankvorm/u-profiel'),
        'w-profiel': KeuzelijstWaarde(invulwaarde='w-profiel',
                                      label='w-profiel',
                                      status='ingebruik',
                                      definitie='w-profiel',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKunststoffenDamplankvorm/w-profiel'),
        'z-profiel': KeuzelijstWaarde(invulwaarde='z-profiel',
                                      label='z-profiel',
                                      status='ingebruik',
                                      definitie='z-profiel',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKunststoffenDamplankvorm/z-profiel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

