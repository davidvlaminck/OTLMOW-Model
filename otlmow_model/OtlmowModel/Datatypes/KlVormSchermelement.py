# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVormSchermelement(KeuzelijstField):
    """Deze keuzelijst geeft aan of het schermelement recht of gebogen is."""
    naam = 'KlVormSchermelement'
    label = 'Vorm schermelement'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormSchermelement'
    definition = 'Deze keuzelijst geeft aan of het schermelement recht of gebogen is.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormSchermelement'
    options = {
        'gebogen': KeuzelijstWaarde(invulwaarde='gebogen',
                                    label='gebogen',
                                    status='ingebruik',
                                    definitie='gebogen',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormSchermelement/gebogen'),
        'recht': KeuzelijstWaarde(invulwaarde='recht',
                                  label='recht',
                                  status='ingebruik',
                                  definitie='recht',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormSchermelement/recht')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

