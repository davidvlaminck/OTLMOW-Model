# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeAnker(KeuzelijstField):
    """De mogelijke type ankers."""
    naam = 'KlTypeAnker'
    label = 'Type anker'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeAnker'
    definition = 'De mogelijke type ankers.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeAnker'
    options = {
        'ingeboord': KeuzelijstWaarde(invulwaarde='ingeboord',
                                      label='ingeboord',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeAnker/ingeboord'),
        'ingestort': KeuzelijstWaarde(invulwaarde='ingestort',
                                      label='ingestort',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeAnker/ingestort'),
        'voorgespannen-ankers-met-tegenplaat': KeuzelijstWaarde(invulwaarde='voorgespannen-ankers-met-tegenplaat',
                                                                label='voorgespannen ankers met tegenplaat',
                                                                status='ingebruik',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeAnker/voorgespannen-ankers-met-tegenplaat')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

