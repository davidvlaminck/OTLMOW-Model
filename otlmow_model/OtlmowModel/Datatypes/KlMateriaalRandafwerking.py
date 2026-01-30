# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalRandafwerking(KeuzelijstField):
    """Het materiaal van de randafwerking."""
    naam = 'KlMateriaalRandafwerking'
    label = 'materiaal randafwerking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMateriaalRandafwerking'
    definition = 'Het materiaal van de randafwerking.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalRandafwerking'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  definitie='Beton',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalRandafwerking/beton'),
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 definitie='Hout',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalRandafwerking/hout'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      definitie='Kunststof',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalRandafwerking/kunststof'),
        'natuursteen': KeuzelijstWaarde(invulwaarde='natuursteen',
                                        label='natuursteen',
                                        status='ingebruik',
                                        definitie='Natuursteen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalRandafwerking/natuursteen'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  definitie='Staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalRandafwerking/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

