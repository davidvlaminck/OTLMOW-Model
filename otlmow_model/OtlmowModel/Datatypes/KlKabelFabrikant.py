# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelFabrikant(KeuzelijstField):
    """Lijst met producenten van kabels."""
    naam = 'KlKabelFabrikant'
    label = 'Kabel fabrikant'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlKabelFabrikant'
    definition = 'Lijst met producenten van kabels.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelFabrikant'
    options = {
        'stl': KeuzelijstWaarde(invulwaarde='stl',
                                label='STL',
                                status='ingebruik',
                                definitie='Sterlite Technologies.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelFabrikant/stl')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

