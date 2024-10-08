# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVoorschakelapparaatType(KeuzelijstField):
    """Type van het voorschakelapparaat."""
    naam = 'KlVoorschakelapparaatType'
    label = 'Voorschakelapparaat type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVoorschakelapparaatType'
    definition = 'Type van het voorschakelapparaat.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVoorschakelapparaatType'
    options = {
        'elektromechanisch': KeuzelijstWaarde(invulwaarde='elektromechanisch',
                                              label='elektromechanisch',
                                              status='ingebruik',
                                              definitie='/ CLASS : IVSB',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoorschakelapparaatType/elektromechanisch'),
        'elektronisch': KeuzelijstWaarde(invulwaarde='elektronisch',
                                         label='elektronisch',
                                         status='ingebruik',
                                         definitie='/ CLASS : IVSB',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoorschakelapparaatType/elektronisch'),
        'niet-gekend': KeuzelijstWaarde(invulwaarde='niet-gekend',
                                        label='Niet gekend',
                                        status='ingebruik',
                                        definitie='Type niet gekend',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoorschakelapparaatType/niet-gekend')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

