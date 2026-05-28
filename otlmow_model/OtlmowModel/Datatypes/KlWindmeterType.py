# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWindmeterType(KeuzelijstField):
    """Types van windmeters."""
    naam = 'KlWindmeterType'
    label = 'Windmeter type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWindmeterType'
    definition = 'Types van windmeters.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWindmeterType'
    options = {
        'ultrasoon': KeuzelijstWaarde(invulwaarde='ultrasoon',
                                      label='Ultrasoon',
                                      status='ingebruik',
                                      definitie='Ultrasoon',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWindmeterType/ultrasoon'),
        'windrichting': KeuzelijstWaarde(invulwaarde='windrichting',
                                         label='windrichting',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWindmeterType/windrichting'),
        'windrichting-en-windsnelheid': KeuzelijstWaarde(invulwaarde='windrichting-en-windsnelheid',
                                                         label='windrichting en windsnelheid',
                                                         status='ingebruik',
                                                         definitie='windrichting en windsnelheid',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWindmeterType/windrichting-en-windsnelheid'),
        'windsnelheid': KeuzelijstWaarde(invulwaarde='windsnelheid',
                                         label='windsnelheid',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWindmeterType/windsnelheid')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

