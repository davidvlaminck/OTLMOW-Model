# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchanskorfVorm(KeuzelijstField):
    """Vormen van schanskorven."""
    naam = 'KlSchanskorfVorm'
    label = 'Schanskorf vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSchanskorfVorm'
    definition = 'Vormen van schanskorven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchanskorfVorm'
    options = {
        'in-blokvorm': KeuzelijstWaarde(invulwaarde='in-blokvorm',
                                        label='in blokvorm',
                                        status='ingebruik',
                                        definitie='in blokvorm',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchanskorfVorm/in-blokvorm'),
        'in-matrasvorm': KeuzelijstWaarde(invulwaarde='in-matrasvorm',
                                          label='in matrasvorm',
                                          status='ingebruik',
                                          definitie='in matrasvorm',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchanskorfVorm/in-matrasvorm')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

