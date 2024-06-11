# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPTRegelaarModuleMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor PTRegelaarModule."""
    naam = 'KlPTRegelaarModuleMerk'
    label = 'PT regelaarmodule merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlPTRegelaarModuleMerk'
    definition = 'Keuzelijst met merknamen voor PTRegelaarModule.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPTRegelaarModuleMerk'
    options = {
        'adeunis': KeuzelijstWaarde(invulwaarde='adeunis',
                                    label='Adeunis',
                                    status='ingebruik',
                                    definitie='Adeunis',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleMerk/adeunis'),
        'moxa': KeuzelijstWaarde(invulwaarde='moxa',
                                 label='Moxa',
                                 status='ingebruik',
                                 definitie='Moxa',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleMerk/moxa'),
        'puls': KeuzelijstWaarde(invulwaarde='puls',
                                 label='Puls',
                                 status='ingebruik',
                                 definitie='Puls',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleMerk/puls'),
        'spie': KeuzelijstWaarde(invulwaarde='spie',
                                 label='Spie',
                                 status='ingebruik',
                                 definitie='Spie',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPTRegelaarModuleMerk/spie')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

