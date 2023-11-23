# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRetroreflecterendeKokerFolieType(KeuzelijstField):
    """Keuzeijst voor het bepalen van folietype van de retroreflecterende koker."""
    naam = 'KlRetroreflecterendeKokerFolieType'
    label = 'Retroreflecterende koker folie type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRetroreflecterendeKokerFolieType'
    definition = 'Keuzeijst voor het bepalen van folietype van de retroreflecterende koker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRetroreflecterendeKokerFolieType'
    options = {
        'type-2': KeuzelijstWaarde(invulwaarde='type-2',
                                   label='type 2',
                                   status='ingebruik',
                                   definitie='Keuze folie type 2 (geel) als folietype van de retroreflecterende koker',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendeKokerFolieType/type-2'),
        'type-3': KeuzelijstWaarde(invulwaarde='type-3',
                                   label='type 3',
                                   status='ingebruik',
                                   definitie='Keuze folie type 3 als folietype (geel - fluorescerend) van de retroreflecterende koker',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendeKokerFolieType/type-3')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

