# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKeuringsresultaat(KeuzelijstField):
    """De mogelijke keuringsresultaten."""
    naam = 'KlKeuringsresultaat'
    label = 'Keuringsresultaat'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKeuringsresultaat'
    definition = 'De mogelijke keuringsresultaten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKeuringsresultaat'
    options = {
        'conform': KeuzelijstWaarde(invulwaarde='conform',
                                    label='conform',
                                    status='ingebruik',
                                    definitie='Het gekeurde object, onderdeel of installatie voldoet aan alle vastgelegde criteria, normen of voorschriften op het moment van de keuring.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKeuringsresultaat/conform'),
        'conform-met-opmerkingen': KeuzelijstWaarde(invulwaarde='conform-met-opmerkingen',
                                                    label='conform met opmerkingen',
                                                    status='ingebruik',
                                                    definitie='Het gekeurde object, onderdeel of installatie voldoet aan alle vastgelegde criteria, normen of voorschriften op het moment van de keuring maar met aanwezige opmerkingen.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKeuringsresultaat/conform-met-opmerkingen'),
        'inbreuken': KeuzelijstWaarde(invulwaarde='inbreuken',
                                      label='inbreuken',
                                      status='ingebruik',
                                      definitie='Het gekeurde object, onderdeel of installatie voldoet niet aan één of meerdere vastgelegde criteria, normen of voorschriften op het moment van de keuring.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKeuringsresultaat/inbreuken'),
        'niet-conform': KeuzelijstWaarde(invulwaarde='niet-conform',
                                         label='niet-conform',
                                         status='verwijderd',
                                         definitie='Het gekeurde object, onderdeel of installatie voldoet niet aan één of meerdere vastgelegde criteria, normen of voorschriften op het moment van de keuring.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKeuringsresultaat/niet-conform')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

