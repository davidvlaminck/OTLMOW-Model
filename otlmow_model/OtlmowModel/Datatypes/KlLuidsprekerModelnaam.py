# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLuidsprekerModelnaam(KeuzelijstField):
    """De modelnaam van de luidspreker."""
    naam = 'KlLuidsprekerModelnaam'
    label = 'Luidspreker modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLuidsprekerModelnaam'
    definition = 'De modelnaam van de luidspreker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLuidsprekerModelnaam'
    options = {
        'abf-260-100w-pa6-v0': KeuzelijstWaarde(invulwaarde='abf-260-100w-pa6-v0',
                                                label='ABF-260/100W PA6 V0',
                                                status='ingebruik',
                                                definitie='ABF-260/100W PA6 V0',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuidsprekerModelnaam/abf-260-100w-pa6-v0'),
        'da-10-260-t-en54': KeuzelijstWaarde(invulwaarde='da-10-260-t-en54',
                                             label='DA 10-260/T-EN54',
                                             status='ingebruik',
                                             definitie='DA 10-260/T-EN54',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuidsprekerModelnaam/da-10-260-t-en54'),
        'dk-30-t-en54-pg': KeuzelijstWaarde(invulwaarde='dk-30-t-en54-pg',
                                            label='DK 30/T-EN54-PG',
                                            status='ingebruik',
                                            definitie='DK 30/T-EN54-PG',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuidsprekerModelnaam/dk-30-t-en54-pg')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

