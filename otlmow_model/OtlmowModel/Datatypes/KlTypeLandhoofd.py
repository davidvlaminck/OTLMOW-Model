# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeLandhoofd(KeuzelijstField):
    """Het type landhoofd."""
    naam = 'KlTypeLandhoofd'
    label = 'Type landhoofd'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeLandhoofd'
    definition = 'Het type landhoofd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeLandhoofd'
    options = {
        'hoog-gefundeerd': KeuzelijstWaarde(invulwaarde='hoog-gefundeerd',
                                            label='hoog gefundeerd',
                                            status='ingebruik',
                                            definitie='hoog gefundeerd',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeLandhoofd/hoog-gefundeerd'),
        'laag-gefundeerd': KeuzelijstWaarde(invulwaarde='laag-gefundeerd',
                                            label='laag gefundeerd',
                                            status='ingebruik',
                                            definitie='laag gefundeerd',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeLandhoofd/laag-gefundeerd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

