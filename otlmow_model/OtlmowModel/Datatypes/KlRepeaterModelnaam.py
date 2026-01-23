# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRepeaterModelnaam(KeuzelijstField):
    """Keuzelijst met modelnamen voor Repeater."""
    naam = 'KlRepeaterModelnaam'
    label = 'repeater modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRepeaterModelnaam'
    definition = 'Keuzelijst met modelnamen voor Repeater.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRepeaterModelnaam'
    options = {
        'lcn7622-01': KeuzelijstWaarde(invulwaarde='lcn7622-01',
                                       label='LCN7622-01',
                                       status='ingebruik',
                                       definitie='LCN7622-01',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRepeaterModelnaam/lcn7622-01')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

