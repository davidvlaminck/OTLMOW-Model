# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSimkaarttype(KeuzelijstField):
    """De mogelijk types van een simkaart."""
    naam = 'KlSimkaarttype'
    label = 'Simkaarttype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSimkaarttype'
    definition = 'De mogelijk types van een simkaart.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSimkaarttype'
    options = {
        'geen': KeuzelijstWaarde(invulwaarde='geen',
                                 label='geen',
                                 status='ingebruik',
                                 definitie='geen simkaart',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSimkaarttype/geen'),
        'olu': KeuzelijstWaarde(invulwaarde='olu',
                                label='OLU',
                                status='ingebruik',
                                definitie='OLU simkaart',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSimkaarttype/olu'),
        'sim-olu': KeuzelijstWaarde(invulwaarde='sim-olu',
                                    label='SIM-OLU',
                                    status='ingebruik',
                                    definitie='SIM-OLU',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSimkaarttype/sim-olu'),
        'standaard': KeuzelijstWaarde(invulwaarde='standaard',
                                      label='standaard',
                                      status='ingebruik',
                                      definitie='standaard simkaart',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSimkaarttype/standaard')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

