# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRackType(KeuzelijstField):
    """Lijst met gestandaardiseerde en niet-gestandaardiseerde types rack in gebruik bij de assetbeheerder."""
    naam = 'KlRackType'
    label = 'rack type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRackType'
    definition = 'Lijst met gestandaardiseerde en niet-gestandaardiseerde types rack in gebruik bij de assetbeheerder.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRackType'
    options = {
        '19-inch': KeuzelijstWaarde(invulwaarde='19-inch',
                                    label='19-inch',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/19-inch'),
        '21-inch': KeuzelijstWaarde(invulwaarde='21-inch',
                                    label='21-inch',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/21-inch'),
        'DIN-rail': KeuzelijstWaarde(invulwaarde='DIN-rail',
                                     label='DIN-rail',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/DIN-rail'),
        'MIVLVERack': KeuzelijstWaarde(invulwaarde='MIVLVERack',
                                       label='MIVLVERack',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/MIVLVERack'),
        'MIVSATRack': KeuzelijstWaarde(invulwaarde='MIVSATRack',
                                       label='MIVSATRack',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/MIVSATRack')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

