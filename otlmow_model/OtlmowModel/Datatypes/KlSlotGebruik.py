# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlotGebruik(KeuzelijstField):
    """Keuzelijst voor de kant langs dewelke het slot geïnstalleerd kan worden. Je kijkt hierbij naar de deur vanuit de kant dat je de deur openduwt (en niet de kant waarlangs je zou moeten trekken)."""
    naam = 'KlSlotGebruik'
    label = 'Slot gebruik'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlotGebruik'
    definition = 'Keuzelijst voor de kant langs dewelke het slot geïnstalleerd kan worden. Je kijkt hierbij naar de deur vanuit de kant dat je de deur openduwt (en niet de kant waarlangs je zou moeten trekken).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlotGebruik'
    options = {
        'links': KeuzelijstWaarde(invulwaarde='links',
                                  label='links',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotGebruik/links'),
        'omkeerbaar': KeuzelijstWaarde(invulwaarde='omkeerbaar',
                                       label='omkeerbaar',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotGebruik/omkeerbaar'),
        'rechts': KeuzelijstWaarde(invulwaarde='rechts',
                                   label='rechts',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSlotGebruik/rechts')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

