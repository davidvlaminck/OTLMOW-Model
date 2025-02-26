# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDrukknopModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Drukknop."""
    naam = 'KlDrukknopModelnaam'
    label = 'Drukknop modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDrukknopModelnaam'
    definition = 'Keuzelijst met modelnamen voor Drukknop.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDrukknopModelnaam'
    options = {
        'daps-2100l-230v': KeuzelijstWaarde(invulwaarde='daps-2100l-230v',
                                            label='DAPS 2100L 230V',
                                            status='ingebruik',
                                            definitie='DAPS 2100L 230V',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopModelnaam/daps-2100l-230v'),
        'daps-2100l-42v': KeuzelijstWaarde(invulwaarde='daps-2100l-42v',
                                           label='DAPS 2100L 42V',
                                           status='ingebruik',
                                           definitie='DAPS 2100L 42V',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopModelnaam/daps-2100l-42v')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

