# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtsensorMerk(KeuzelijstField):
    """Lichtsensor merken."""
    naam = 'KlLichtsensorMerk'
    label = 'Lichtsensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtsensorMerk'
    definition = 'Lichtsensor merken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtsensorMerk'
    options = {
        'electrical-special': KeuzelijstWaarde(invulwaarde='electrical-special',
                                               label='ELECTRICAL-SPECIAL',
                                               status='ingebruik',
                                               definitie='ELECTRICAL-SPECIAL',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtsensorMerk/electrical-special'),
        'philips': KeuzelijstWaarde(invulwaarde='philips',
                                    label='Philips',
                                    status='ingebruik',
                                    definitie='Philips',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtsensorMerk/philips'),
        'schreder': KeuzelijstWaarde(invulwaarde='schreder',
                                     label='Schreder',
                                     status='ingebruik',
                                     definitie='Schreder',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtsensorMerk/schreder'),
        'skye': KeuzelijstWaarde(invulwaarde='skye',
                                 label='Skye',
                                 status='ingebruik',
                                 definitie='Skye',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtsensorMerk/skye')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

