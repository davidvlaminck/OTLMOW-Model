# coding=utf-8
from types import MappingProxyType
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDetectieVeModelnaam(KeuzelijstField):
    """De mogelijke opties voor de modelnaam van een detectieverwerkingseenheid."""
    naam = 'KlDetectieVeModelnaam'
    label = 'Detectieverwerkingseenheid modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDetectieVeModelnaam'
    definition = 'De mogelijke opties voor de modelnaam van een detectieverwerkingseenheid.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDetectieVeModelnaam'
    options: MappingProxyType[str, KeuzelijstWaarde] = MappingProxyType({
        '1ti': KeuzelijstWaarde(invulwaarde='1ti',
                                label='1TI',
                                status='ingebruik',
                                definitie='1TI',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectieVeModelnaam/1ti'),
        '4ti': KeuzelijstWaarde(invulwaarde='4ti',
                                label='4TI',
                                status='ingebruik',
                                definitie='4TI',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectieVeModelnaam/4ti'),
        'ti-bpl2': KeuzelijstWaarde(invulwaarde='ti-bpl2',
                                    label='TI BPL2',
                                    status='ingebruik',
                                    definitie='TI BPL2',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectieVeModelnaam/ti-bpl2'),
        'ti-bpl3': KeuzelijstWaarde(invulwaarde='ti-bpl3',
                                    label='TI BPL3',
                                    status='ingebruik',
                                    definitie='TI BPL3',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDetectieVeModelnaam/ti-bpl3')
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

