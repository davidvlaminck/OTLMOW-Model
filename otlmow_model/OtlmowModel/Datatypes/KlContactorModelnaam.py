# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactorModelnaam(KeuzelijstField):
    """Keuzelijst met modelnaen van de contactoren volgens de fabrikanten."""
    naam = 'KlContactorModelnaam'
    label = 'Contactor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactorModelnaam'
    definition = 'Keuzelijst met modelnaen van de contactoren volgens de fabrikanten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactorModelnaam'
    options = {
        'drm': KeuzelijstWaarde(invulwaarde='drm',
                                label='DRM',
                                status='ingebruik',
                                definitie='DRM',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactorModelnaam/drm'),
        'lc1': KeuzelijstWaarde(invulwaarde='lc1',
                                label='LC1',
                                status='ingebruik',
                                definitie='LC1',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactorModelnaam/lc1')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

