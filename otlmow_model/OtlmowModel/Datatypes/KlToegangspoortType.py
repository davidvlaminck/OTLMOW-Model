# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangspoortType(KeuzelijstField):
    """Lijst met types voor toegangspoorten volgens de manier waarop de poort opent."""
    naam = 'KlToegangspoortType'
    label = 'Toegangspoort type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToegangspoortType'
    definition = 'Lijst met types voor toegangspoorten volgens de manier waarop de poort opent.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangspoortType'
    options = {
        'draaipoort': KeuzelijstWaarde(invulwaarde='draaipoort',
                                       label='draaipoort',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangspoortType/draaipoort'),
        'schuifpoort': KeuzelijstWaarde(invulwaarde='schuifpoort',
                                        label='schuifpoort',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangspoortType/schuifpoort'),
        'vleugelpoort': KeuzelijstWaarde(invulwaarde='vleugelpoort',
                                         label='vleugelpoort',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangspoortType/vleugelpoort')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

