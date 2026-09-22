# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBeschermlaag(KeuzelijstField):
    """De mogelijke types beschermlaag."""
    naam = 'KlTypeBeschermlaag'
    label = 'Type beschermlaag'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeBeschermlaag'
    definition = 'De mogelijke types beschermlaag.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBeschermlaag'
    options = {
        'apo-c': KeuzelijstWaarde(invulwaarde='apo-c',
                                  label='APO-C',
                                  status='ingebruik',
                                  definitie='APO-C',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschermlaag/apo-c'),
        'apo-d': KeuzelijstWaarde(invulwaarde='apo-d',
                                  label='APO-D',
                                  status='ingebruik',
                                  definitie='APO-D',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschermlaag/apo-d'),
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  definitie='beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschermlaag/beton'),
        'gab-d': KeuzelijstWaarde(invulwaarde='gab-d',
                                  label='GAB-D',
                                  status='ingebruik',
                                  definitie='GAB-D',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschermlaag/gab-d'),
        'gewapende-bitumeneuze-membraan': KeuzelijstWaarde(invulwaarde='gewapende-bitumeneuze-membraan',
                                                           label='gewapende bitumeneuze membraan',
                                                           status='ingebruik',
                                                           definitie='gewapende bitumeneuze membraan',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschermlaag/gewapende-bitumeneuze-membraan'),
        'hars': KeuzelijstWaarde(invulwaarde='hars',
                                 label='hars',
                                 status='ingebruik',
                                 definitie='hars',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBeschermlaag/hars')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

