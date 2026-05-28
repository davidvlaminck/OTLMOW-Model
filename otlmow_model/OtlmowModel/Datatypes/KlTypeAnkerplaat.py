# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeAnkerplaat(KeuzelijstField):
    """Lijst met de verschilende types van een ankerplaat"""
    naam = 'KlTypeAnkerplaat'
    label = 'Type ankerplaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeAnkerplaat'
    definition = 'Lijst met de verschilende types van een ankerplaat'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeAnkerplaat'
    options = {
        'ingestort': KeuzelijstWaarde(invulwaarde='ingestort',
                                      label='ingestort',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeAnkerplaat/ingestort'),
        'niet-ingestort': KeuzelijstWaarde(invulwaarde='niet-ingestort',
                                           label='niet-ingestort',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeAnkerplaat/niet-ingestort'),
        'voorgespannen': KeuzelijstWaarde(invulwaarde='voorgespannen',
                                          label='voorgespannen',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeAnkerplaat/voorgespannen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

