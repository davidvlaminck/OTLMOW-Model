# coding=utf-8
from types import MappingProxyType
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoEcoductType(KeuzelijstField):
    """Types van ecoduct."""
    naam = 'KlEcoEcoductType'
    label = 'Ecoduct type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoEcoductType'
    definition = 'Types van ecoduct.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoEcoductType'
    options: MappingProxyType[str, KeuzelijstWaarde] = MappingProxyType({
        'bermbrug': KeuzelijstWaarde(invulwaarde='bermbrug',
                                     label='bermbrug',
                                     status='ingebruik',
                                     definitie='Een bestaande, vaak smalle brug met beperkt verkeer waarop de natuur via groene bermen doorloopt.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcoductType/bermbrug'),
        'ecocreaduct': KeuzelijstWaarde(invulwaarde='ecocreaduct',
                                        label='ecocreaduct',
                                        status='ingebruik',
                                        definitie='Een brug hoofdzakelijk in gebruik voor natuur, gecombineerd met zachte recreatie (fietsers, wandelaars, ruiters).',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcoductType/ecocreaduct'),
        'ecoveloduct': KeuzelijstWaarde(invulwaarde='ecoveloduct',
                                        label='ecoveloduct',
                                        status='ingebruik',
                                        definitie='Een brug hoofdzakelijk in gebruik voor natuur, gecombineerd met een fietspad.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcoductType/ecoveloduct')
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

