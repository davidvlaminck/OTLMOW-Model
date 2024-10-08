# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAardWBSS(KeuzelijstField):
    """De mogelijke vormen die ervoor zorgen dat hemelwater infiltreert langs de waterdoorlatende betonstraatsteen."""
    naam = 'KlAardWBSS'
    label = 'Aard van waterdoorlatende betonstraatsteen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAardWBSS'
    definition = 'De mogelijke vormen die ervoor zorgen dat hemelwater infiltreert langs de waterdoorlatende betonstraatsteen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAardWBSS'
    options = {
        'met-drainageopeningen': KeuzelijstWaarde(invulwaarde='met-drainageopeningen',
                                                  label='met drainageopeningen',
                                                  status='ingebruik',
                                                  definitie='Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert langs de betonstraatsteen.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/met-drainageopeningen'),
        'met-verbrede-voegen': KeuzelijstWaarde(invulwaarde='met-verbrede-voegen',
                                                label='met verbrede voegen',
                                                status='ingebruik',
                                                definitie='Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert langs de betonstraatsteen.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/met-verbrede-voegen'),
        'poreus-beton': KeuzelijstWaarde(invulwaarde='poreus-beton',
                                         label='poreus beton',
                                         status='ingebruik',
                                         definitie='Vorm voor waterdoorlatende betonstraatsteen waarbij hemelwater infiltreert doorheen de betonstraatsteen.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAardWBSS/poreus-beton')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

