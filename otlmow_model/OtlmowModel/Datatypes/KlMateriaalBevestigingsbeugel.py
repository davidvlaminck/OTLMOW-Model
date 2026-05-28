# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalBevestigingsbeugel(KeuzelijstField):
    """De verschillende opties materiaal waaruit de bevestigingsbeugel kan bestaan."""
    naam = 'KlMateriaalBevestigingsbeugel'
    label = 'materiaal bevestigingsbeugel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlMateriaalBevestigingsbeugel'
    definition = 'De verschillende opties materiaal waaruit de bevestigingsbeugel kan bestaan.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalBevestigingsbeugel'
    options = {
        'pe': KeuzelijstWaarde(invulwaarde='pe',
                               label='PE',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBevestigingsbeugel/pe'),
        'pp': KeuzelijstWaarde(invulwaarde='pp',
                               label='PP',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBevestigingsbeugel/pp'),
        'pvc': KeuzelijstWaarde(invulwaarde='pvc',
                                label='PVC',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBevestigingsbeugel/pvc'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBevestigingsbeugel/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

