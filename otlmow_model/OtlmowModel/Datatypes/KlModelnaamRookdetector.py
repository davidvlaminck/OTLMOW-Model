# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlModelnaamRookdetector(KeuzelijstField):
    """De modelnaam van de rookdetector."""
    naam = 'KlModelnaamRookdetector'
    label = 'modelnaam rookdetector'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlModelnaamRookdetector'
    definition = 'De modelnaam van de rookdetector.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlModelnaamRookdetector'
    options = {
        'ke-dp3120w': KeuzelijstWaarde(invulwaarde='ke-dp3120w',
                                       label='KE-DP3120W',
                                       status='ingebruik',
                                       definitie='KE-DP3120W',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlModelnaamRookdetector/ke-dp3120w'),
        'ke-dp3120w-sn': KeuzelijstWaarde(invulwaarde='ke-dp3120w-sn',
                                          label='KE-DP3120W-SN',
                                          status='ingebruik',
                                          definitie='KE-DP3120W-SN',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlModelnaamRookdetector/ke-dp3120w-sn'),
        'ke-dp3120w-snv': KeuzelijstWaarde(invulwaarde='ke-dp3120w-snv',
                                           label='KE-DP3120W-SNV',
                                           status='ingebruik',
                                           definitie='KE-DP3120W-SNV',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlModelnaamRookdetector/ke-dp3120w-snv')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

