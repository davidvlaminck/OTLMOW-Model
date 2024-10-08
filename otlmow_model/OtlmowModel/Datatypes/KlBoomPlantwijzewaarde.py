# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomPlantwijzewaarde(KeuzelijstField):
    """De verschillende opties van de plantwijzewaarde."""
    naam = 'KlBoomPlantwijzewaarde'
    label = 'Boom plantwijzewaarde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomPlantwijzewaarde'
    definition = 'De verschillende opties van de plantwijzewaarde.'
    status = 'ingebruik'
    deprecated_version = '2.12.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomPlantwijzewaarde'
    options = {
        '0.4': KeuzelijstWaarde(invulwaarde='0.4',
                                label='0.4',
                                status='ingebruik',
                                definitie='boom in grote dicht beplante groepen (> 10 stuks) (ook bosachtige beplantingen, bospark)',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/0.4'),
        '0.6': KeuzelijstWaarde(invulwaarde='0.6',
                                label='0.6',
                                status='ingebruik',
                                definitie='boom in groep van 6 - 10 stuks',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/0.6'),
        '0.7': KeuzelijstWaarde(invulwaarde='0.7',
                                label='0.7',
                                status='ingebruik',
                                definitie='boom in groep van 2 - 5 stuks',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/0.7'),
        '0.8': KeuzelijstWaarde(invulwaarde='0.8',
                                label='0.8',
                                status='ingebruik',
                                definitie='rijbeplanting met belangrijke uitval',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/0.8'),
        '0.9': KeuzelijstWaarde(invulwaarde='0.9',
                                label='0.9',
                                status='ingebruik',
                                definitie='perfecte rijbeplanting (zonder uitval)',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/0.9'),
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie='solitaire plant',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/1')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

