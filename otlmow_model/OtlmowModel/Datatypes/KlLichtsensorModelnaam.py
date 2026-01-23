# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtsensorModelnaam(KeuzelijstField):
    """Lichtsensor modelnamen."""
    naam = 'KlLichtsensorModelnaam'
    label = 'Lichtsensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtsensorModelnaam'
    definition = 'Lichtsensor modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtsensorModelnaam'
    options = {
        'lrl7621': KeuzelijstWaarde(invulwaarde='lrl7621',
                                    label='LRL7621',
                                    status='ingebruik',
                                    definitie='LRL7621',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtsensorModelnaam/lrl7621'),
        'luminance-luci-l20': KeuzelijstWaarde(invulwaarde='luminance-luci-l20',
                                               label='Luminance LUCI L20',
                                               status='ingebruik',
                                               definitie='Luminance LUCI L20',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtsensorModelnaam/luminance-luci-l20'),
        'skl2638': KeuzelijstWaarde(invulwaarde='skl2638',
                                    label='SKL2638',
                                    status='ingebruik',
                                    definitie='SKL2638',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtsensorModelnaam/skl2638')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

