# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCOpeningType(KeuzelijstField):
    """Types van opening."""
    naam = 'KlLEGCOpeningType'
    label = 'Opening type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCOpeningType'
    definition = 'Types van opening.'
    status = 'ingebruik'
    deprecated_version = '2.1.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCOpeningType'
    options = {
        'dienstopening': KeuzelijstWaarde(invulwaarde='dienstopening',
                                          label='dienstopening',
                                          status='verwijderd',
                                          definitie='dienstopening',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/dienstopening'),
        'nooddeur': KeuzelijstWaarde(invulwaarde='nooddeur',
                                     label='nooddeur',
                                     status='verwijderd',
                                     definitie="Deze optie mag niet geselecteerd worden. Indien de doorgang een nooddeur is moet het onderdeel 'Vluchtdeur' geïnstantieerd worden ipv het onderdeel 'Doorgang'. ",
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/nooddeur'),
        'sas': KeuzelijstWaarde(invulwaarde='sas',
                                label='sas',
                                status='verwijderd',
                                definitie='sas',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/sas'),
        'vluchtopening': KeuzelijstWaarde(invulwaarde='vluchtopening',
                                          label='vluchtopening',
                                          status='verwijderd',
                                          definitie='vluchtopening',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/vluchtopening')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

