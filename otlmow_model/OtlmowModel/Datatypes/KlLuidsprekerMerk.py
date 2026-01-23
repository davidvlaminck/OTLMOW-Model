# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLuidsprekerMerk(KeuzelijstField):
    """Het merk van de luidspreker."""
    naam = 'KlLuidsprekerMerk'
    label = 'Luidspreker merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLuidsprekerMerk'
    definition = 'Het merk van de luidspreker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLuidsprekerMerk'
    options = {
        'harman': KeuzelijstWaarde(invulwaarde='harman',
                                   label='Harman',
                                   status='ingebruik',
                                   definitie='Harman',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuidsprekerMerk/harman'),
        'ic-audio': KeuzelijstWaarde(invulwaarde='ic-audio',
                                     label='IC Audio',
                                     status='ingebruik',
                                     definitie='IC Audio',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuidsprekerMerk/ic-audio')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

