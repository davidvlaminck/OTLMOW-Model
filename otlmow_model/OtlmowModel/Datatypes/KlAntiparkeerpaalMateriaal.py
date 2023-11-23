# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAntiparkeerpaalMateriaal(KeuzelijstField):
    """Bepaling van het vervaardigingsmateriaal van de antiparkeerpaal."""
    naam = 'KlAntiparkeerpaalMateriaal'
    label = 'Antiparkeerpaal materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAntiparkeerpaalMateriaal'
    definition = 'Bepaling van het vervaardigingsmateriaal van de antiparkeerpaal.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAntiparkeerpaalMateriaal'
    options = {
        'hout': KeuzelijstWaarde(invulwaarde='hout',
                                 label='hout',
                                 status='ingebruik',
                                 definitie='Keuze hout voor het antiparkeerpaal materiaal.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/hout'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      definitie='Keuze kunststof voor het antiparkeerpaal materiaal.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/kunststof'),
        'metaal': KeuzelijstWaarde(invulwaarde='metaal',
                                   label='metaal',
                                   status='ingebruik',
                                   definitie='Keuze metaal voor het antiparkeerpaal materiaal.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAntiparkeerpaalMateriaal/metaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

