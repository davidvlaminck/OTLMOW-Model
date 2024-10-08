# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWildreflectorDrager(KeuzelijstField):
    """Mogelijke dragers van een wildreflector."""
    naam = 'KlWildreflectorDrager'
    label = 'Wildreflector drager'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWildreflectorDrager'
    definition = 'Mogelijke dragers van een wildreflector.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWildreflectorDrager'
    options = {
        'houten-paal': KeuzelijstWaarde(invulwaarde='houten-paal',
                                        label='houten paal',
                                        status='ingebruik',
                                        definitie='houten paal als drager.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWildreflectorDrager/houten-paal'),
        'metalen-paal': KeuzelijstWaarde(invulwaarde='metalen-paal',
                                         label='metalen paal',
                                         status='ingebruik',
                                         definitie='metalen paal als drager.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWildreflectorDrager/metalen-paal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

