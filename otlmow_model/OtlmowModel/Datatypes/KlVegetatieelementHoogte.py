# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVegetatieelementHoogte(KeuzelijstField):
    """De orde van hoogte van een vegetatie-element."""
    naam = 'KlVegetatieelementHoogte'
    label = 'Vegetatieelement hoogte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVegetatieelementHoogte'
    definition = 'De orde van hoogte van een vegetatie-element.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVegetatieelementHoogte'
    options = {
        '0--7-meter': KeuzelijstWaarde(invulwaarde='0--7-meter',
                                       label='0 -7 meter',
                                       status='ingebruik',
                                       definitie='0 -7 meter',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementHoogte/0--7-meter'),
        '7---20-meter': KeuzelijstWaarde(invulwaarde='7---20-meter',
                                         label='7 - 20 meter',
                                         status='ingebruik',
                                         definitie='7 - 20 meter',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementHoogte/7---20-meter'),
        'groter-dan-20-meter': KeuzelijstWaarde(invulwaarde='groter-dan-20-meter',
                                                label='groter dan 20 meter',
                                                status='ingebruik',
                                                definitie='> 20 meter',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVegetatieelementHoogte/groter-dan-20-meter')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

