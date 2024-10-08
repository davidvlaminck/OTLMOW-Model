# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAardingsInstallatieType(KeuzelijstField):
    """Een keuzelijst waarin aangeduid kan worden over welke aardingsinstallatietype het gaat."""
    naam = 'KlAardingsInstallatieType'
    label = 'Type van aardingsinstallatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlAardingsInstallatieType'
    definition = 'Een keuzelijst waarin aangeduid kan worden over welke aardingsinstallatietype het gaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAardingsInstallatieType'
    options = {
        'hoogspanningsinstallatie': KeuzelijstWaarde(invulwaarde='hoogspanningsinstallatie',
                                                     label='hoogspanningsinstallatie',
                                                     status='ingebruik',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingsInstallatieType/hoogspanningsinstallatie'),
        'laagspanningsinstallatie': KeuzelijstWaarde(invulwaarde='laagspanningsinstallatie',
                                                     label='laagspanningsinstallatie',
                                                     status='ingebruik',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingsInstallatieType/laagspanningsinstallatie'),
        'nulpuntinstallatie': KeuzelijstWaarde(invulwaarde='nulpuntinstallatie',
                                               label='nulpuntinstallatie',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardingsInstallatieType/nulpuntinstallatie')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

