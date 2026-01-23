# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNoodstopknopModelnaam(KeuzelijstField):
    """De modelnaam van een noodstopknop."""
    naam = 'KlNoodstopknopModelnaam'
    label = 'Noodstopknop modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNoodstopknopModelnaam'
    definition = 'De modelnaam van een noodstopknop.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNoodstopknopModelnaam'
    options = {
        'xb4': KeuzelijstWaarde(invulwaarde='xb4',
                                label='XB4',
                                status='ingebruik',
                                definitie='XB4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNoodstopknopModelnaam/xb4')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

