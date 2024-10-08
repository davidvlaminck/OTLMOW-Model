# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOBitSnelheid(KeuzelijstField):
    """Lijst met mogelijke bitsnelheden voor een invoer-uitvoer kaart of module."""
    naam = 'KlIOBitSnelheid'
    label = 'IO bit snelheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOBitSnelheid'
    definition = 'Lijst met mogelijke bitsnelheden voor een invoer-uitvoer kaart of module.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOBitSnelheid'
    options = {
        '16': KeuzelijstWaarde(invulwaarde='16',
                               label='16',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOBitSnelheid/16'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOBitSnelheid/2'),
        '32': KeuzelijstWaarde(invulwaarde='32',
                               label='32',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOBitSnelheid/32'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOBitSnelheid/4'),
        '8': KeuzelijstWaarde(invulwaarde='8',
                              label='8',
                              status='ingebruik',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOBitSnelheid/8')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

