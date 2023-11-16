# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElektromotorBouwvorm(KeuzelijstField):
    """Keuzelijst voor de bouwvorm van een elektromotor volgens de IM-code (International Mounting)."""
    naam = 'KlElektromotorBouwvorm'
    label = 'Elektromotor bouwvorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlElektromotorBouwvorm'
    definition = 'Keuzelijst voor de bouwvorm van een elektromotor volgens de IM-code (International Mounting).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElektromotorBouwvorm'
    options = {
        'im-b14---im-3601': KeuzelijstWaarde(invulwaarde='im-b14---im-3601',
                                             label='IM B14 / IM 3601',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-b14---im-3601'),
        'im-b3---im-1001': KeuzelijstWaarde(invulwaarde='im-b3---im-1001',
                                            label='IM B3 / IM 1001',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-b3---im-1001'),
        'im-b34---im-2101': KeuzelijstWaarde(invulwaarde='im-b34---im-2101',
                                             label='IM B34 / IM 2101',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-b34---im-2101'),
        'im-b35---im-2001': KeuzelijstWaarde(invulwaarde='im-b35---im-2001',
                                             label='IM B35 / IM 2001',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-b35---im-2001'),
        'im-b5---im-3001': KeuzelijstWaarde(invulwaarde='im-b5---im-3001',
                                            label='IM B5 / IM 3001',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-b5---im-3001'),
        'im-b6---im-1051': KeuzelijstWaarde(invulwaarde='im-b6---im-1051',
                                            label='IM B6 / IM 1051',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-b6---im-1051'),
        'im-b7---im-1061': KeuzelijstWaarde(invulwaarde='im-b7---im-1061',
                                            label='IM B7 / IM 1061',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-b7---im-1061'),
        'im-b8---im-1071': KeuzelijstWaarde(invulwaarde='im-b8---im-1071',
                                            label='IM B8 / IM 1071',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-b8---im-1071'),
        'im-v1---im-3011': KeuzelijstWaarde(invulwaarde='im-v1---im-3011',
                                            label='IM V1 / IM 3011',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-v1---im-3011'),
        'im-v15---im-2011': KeuzelijstWaarde(invulwaarde='im-v15---im-2011',
                                             label='IM V15 / IM 2011',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-v15---im-2011'),
        'im-v18---im-3611': KeuzelijstWaarde(invulwaarde='im-v18---im-3611',
                                             label='IM V18 / IM 3611',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-v18---im-3611'),
        'im-v19---im-3631': KeuzelijstWaarde(invulwaarde='im-v19---im-3631',
                                             label='IM V19 / IM 3631',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-v19---im-3631'),
        'im-v3---im-3031': KeuzelijstWaarde(invulwaarde='im-v3---im-3031',
                                            label='IM V3 / IM 3031',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-v3---im-3031'),
        'im-v36---im-2031': KeuzelijstWaarde(invulwaarde='im-v36---im-2031',
                                             label='IM V36 / IM 2031',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-v36---im-2031'),
        'im-v5---im-1011': KeuzelijstWaarde(invulwaarde='im-v5---im-1011',
                                            label='IM V5 / IM 1011',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-v5---im-1011'),
        'im-v6---im-1031': KeuzelijstWaarde(invulwaarde='im-v6---im-1031',
                                            label='IM V6 / IM 1031',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElektromotorBouwvorm/im-v6---im-1031')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

