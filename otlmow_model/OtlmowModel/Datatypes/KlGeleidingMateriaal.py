# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGeleidingMateriaal(KeuzelijstField):
    """Materialen voor de geleidingwand om kleinere wilde dieren te geleiden."""
    naam = 'KlGeleidingMateriaal'
    label = 'Geleiding materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGeleidingMateriaal'
    definition = 'Materialen voor de geleidingwand om kleinere wilde dieren te geleiden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGeleidingMateriaal'
    options = {
        'beton': KeuzelijstWaarde(invulwaarde='beton',
                                  label='beton',
                                  status='ingebruik',
                                  definitie='Geleiding bestaande uit een betonnen wand.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeleidingMateriaal/beton'),
        'kunststof': KeuzelijstWaarde(invulwaarde='kunststof',
                                      label='kunststof',
                                      status='ingebruik',
                                      definitie='Geleiding bestaande uit een kunststoffen wand.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeleidingMateriaal/kunststof'),
        'metaal': KeuzelijstWaarde(invulwaarde='metaal',
                                   label='metaal',
                                   status='ingebruik',
                                   definitie='Geleiding bestaande uit een metalen wand.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeleidingMateriaal/metaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

