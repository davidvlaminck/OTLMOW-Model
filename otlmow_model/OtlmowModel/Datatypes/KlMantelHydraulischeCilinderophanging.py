# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMantelHydraulischeCilinderophanging(KeuzelijstField):
    """De wijze van ophanging van de mantel van een hydraulische cilinder."""
    naam = 'KlMantelHydraulischeCilinderophanging'
    label = 'Mantel hydraulische Cinlinderophanging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMantelHydraulischeCilinderophanging'
    definition = 'De wijze van ophanging van de mantel van een hydraulische cilinder.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMantelHydraulischeCilinderophanging'
    options: MappingProxyType[str, KeuzelijstWaarde] = MappingProxyType({
        'astappen': KeuzelijstWaarde(invulwaarde='astappen',
                                     label='astappen',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMantelHydraulischeCilinderophanging/astappen'),
        'eindoog': KeuzelijstWaarde(invulwaarde='eindoog',
                                    label='eindoog',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMantelHydraulischeCilinderophanging/eindoog')
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

