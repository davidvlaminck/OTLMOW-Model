# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalAfdichting(KeuzelijstField):
    """De verschillende opties materiaal waaruit de afdichting kan bestaan."""
    naam = 'KlMateriaalAfdichting'
    label = 'materiaal afdichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlMateriaalAfdichting'
    definition = 'De verschillende opties materiaal waaruit de afdichting kan bestaan.'
    status = 'ingebruik'
    deprecated_version = '2.20.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalAfdichting'
    options = {
        'hars': KeuzelijstWaarde(invulwaarde='hars',
                                 label='hars',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalAfdichting/hars'),
        'hechtend-gietasfalt': KeuzelijstWaarde(invulwaarde='hechtend-gietasfalt',
                                                label='hechtend gietasfalt',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalAfdichting/hechtend-gietasfalt'),
        'niet-hechtend-gietasfalt': KeuzelijstWaarde(invulwaarde='niet-hechtend-gietasfalt',
                                                     label='niet-hechtend gietasfalt',
                                                     status='ingebruik',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalAfdichting/niet-hechtend-gietasfalt'),
        'roofing': KeuzelijstWaarde(invulwaarde='roofing',
                                    label='roofing',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalAfdichting/roofing')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

