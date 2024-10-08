# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeegcomputerModelnaam(KeuzelijstField):
    """De modelnaam van de weegcomputer."""
    naam = 'KlWeegcomputerModelnaam'
    label = 'Modelnaam weegcomputer'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegcomputerModelnaam'
    definition = 'De modelnaam van de weegcomputer.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegcomputerModelnaam'
    options = {
        'maxxis-5-pr5900': KeuzelijstWaarde(invulwaarde='maxxis-5-pr5900',
                                            label='Maxxis 5 PR5900',
                                            status='ingebruik',
                                            definitie='Maxxis 5 PR5900',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegcomputerModelnaam/maxxis-5-pr5900')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

