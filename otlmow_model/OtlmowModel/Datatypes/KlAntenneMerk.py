# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntenneMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Antenne."""
    naam = 'KlAntenneMerk'
    label = 'Antenne merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntenneMerk'
    definition = 'Keuzelijst met merknamen voor Antenne.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntenneMerk'
    options = {
        'panorama-antennas': KeuzelijstWaarde(invulwaarde='panorama-antennas',
                                              label='Panorama Antennas',
                                              status='ingebruik',
                                              definitie='Panorama Antennas',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntenneMerk/panorama-antennas')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

