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
        'b-cables': KeuzelijstWaarde(invulwaarde='b-cables',
                                     label='B-Cables',
                                     status='ingebruik',
                                     definitie='B-Cables',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelFabrikant/b-cables'),
        'eldra': KeuzelijstWaarde(invulwaarde='eldra',
                                  label='Eldra',
                                  status='ingebruik',
                                  definitie='Eldra',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelFabrikant/eldra'),
        'eupen': KeuzelijstWaarde(invulwaarde='eupen',
                                  label='Eupen',
                                  status='ingebruik',
                                  definitie='Eupen',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelFabrikant/eupen'),
        'stl': KeuzelijstWaarde(invulwaarde='stl',
                                label='STL',
                                status='ingebruik',
                                definitie='Sterlite Technologies.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelFabrikant/stl')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

