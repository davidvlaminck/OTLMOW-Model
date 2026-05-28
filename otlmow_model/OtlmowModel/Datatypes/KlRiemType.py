# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRiemType(KeuzelijstField):
    """Keuzelijst voor het type riem."""
    naam = 'KlRiemType'
    label = 'Riem type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRiemType'
    definition = 'Keuzelijst voor het type riem.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRiemType'
    options = {
        'getande-riem': KeuzelijstWaarde(invulwaarde='getande-riem',
                                         label='getande riem',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRiemType/getande-riem'),
        'platte-riem': KeuzelijstWaarde(invulwaarde='platte-riem',
                                        label='platte riem',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRiemType/platte-riem'),
        'v-riem': KeuzelijstWaarde(invulwaarde='v-riem',
                                   label='V-riem',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRiemType/v-riem')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

