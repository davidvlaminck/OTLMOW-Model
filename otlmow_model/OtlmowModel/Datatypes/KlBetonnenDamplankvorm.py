# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBetonnenDamplankvorm(KeuzelijstField):
    """De vorm van de betonnen damplank."""
    naam = 'KlBetonnenDamplankvorm'
    label = 'Betonnen damplankvorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBetonnenDamplankvorm'
    definition = 'De vorm van de betonnen damplank.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBetonnenDamplankvorm'
    options = {
        'cassette': KeuzelijstWaarde(invulwaarde='cassette',
                                     label='cassette',
                                     status='ingebruik',
                                     definitie='cassette',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonnenDamplankvorm/cassette'),
        'hoekplank': KeuzelijstWaarde(invulwaarde='hoekplank',
                                      label='hoekplank',
                                      status='ingebruik',
                                      definitie='hoekplank',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonnenDamplankvorm/hoekplank'),
        'plat': KeuzelijstWaarde(invulwaarde='plat',
                                 label='plat',
                                 status='ingebruik',
                                 definitie='plat',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonnenDamplankvorm/plat'),
        'u-profiel': KeuzelijstWaarde(invulwaarde='u-profiel',
                                      label='u-profiel',
                                      status='ingebruik',
                                      definitie='u-profiel',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonnenDamplankvorm/u-profiel')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

