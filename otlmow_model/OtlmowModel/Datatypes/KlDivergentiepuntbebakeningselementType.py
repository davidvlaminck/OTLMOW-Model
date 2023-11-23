# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDivergentiepuntbebakeningselementType(KeuzelijstField):
    """De vormen van het divergentiepuntbebakeningselement."""
    naam = 'KlDivergentiepuntbebakeningselementType'
    label = 'Divergentiepuntbebakeningselementtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDivergentiepuntbebakeningselementType'
    definition = 'De vormen van het divergentiepuntbebakeningselement.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDivergentiepuntbebakeningselementType'
    options = {
        'klein-model': KeuzelijstWaarde(invulwaarde='klein-model',
                                        label='klein model',
                                        status='ingebruik',
                                        definitie='Divergentiepuntbebakeningselement van 1 meter diameter (folie type 3.a).',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDivergentiepuntbebakeningselementType/klein-model'),
        'standaard-model': KeuzelijstWaarde(invulwaarde='standaard-model',
                                            label='standaard model',
                                            status='ingebruik',
                                            definitie='Divergentiepuntbebakeningselement van 2 meter diameter (folie type 2).',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDivergentiepuntbebakeningselementType/standaard-model')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

