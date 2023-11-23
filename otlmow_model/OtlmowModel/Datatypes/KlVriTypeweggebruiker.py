# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriTypeweggebruiker(KeuzelijstField):
    """Lijst met types van weggebruikers."""
    naam = 'KlVriTypeweggebruiker'
    label = 'VRI detector typeweggebruiker'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVriTypeweggebruiker'
    definition = 'Lijst met types van weggebruikers.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriTypeweggebruiker'
    options = {
        'bus': KeuzelijstWaarde(invulwaarde='bus',
                                label='bus',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/bus'),
        'fiets': KeuzelijstWaarde(invulwaarde='fiets',
                                  label='fiets',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/fiets'),
        'tram': KeuzelijstWaarde(invulwaarde='tram',
                                 label='tram',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/tram'),
        'voertuig': KeuzelijstWaarde(invulwaarde='voertuig',
                                     label='voertuig',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/voertuig'),
        'voetganger': KeuzelijstWaarde(invulwaarde='voetganger',
                                       label='voetganger',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/voetganger'),
        'vrachtwagen': KeuzelijstWaarde(invulwaarde='vrachtwagen',
                                        label='vrachtwagen',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/vrachtwagen')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

