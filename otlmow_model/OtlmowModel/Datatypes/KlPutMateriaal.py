# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPutMateriaal(KeuzelijstField):
    """Vervaardigingsmaterialen van de put."""
    naam = 'KlPutMateriaal'
    label = 'Put materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPutMateriaal'
    definition = 'Vervaardigingsmaterialen van de put.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPutMateriaal'
    options = {
        'PE-of-PP': KeuzelijstWaarde(invulwaarde='PE-of-PP',
                                     label='PE of PP',
                                     status='ingebruik',
                                     definitie='PE of PP',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/PE-of-PP'),
        'beton-of-gres': KeuzelijstWaarde(invulwaarde='beton-of-gres',
                                          label='beton of gres',
                                          status='ingebruik',
                                          definitie='beton of gres',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/beton-of-gres'),
        'beton-of-metselwerk': KeuzelijstWaarde(invulwaarde='beton-of-metselwerk',
                                                label='beton of metselwerk',
                                                status='ingebruik',
                                                definitie='beton of metselwerk',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/beton-of-metselwerk'),
        'glasvezelversterkt-polyesterhars': KeuzelijstWaarde(invulwaarde='glasvezelversterkt-polyesterhars',
                                                             label='glasvezelversterkt polyesterhars',
                                                             status='ingebruik',
                                                             definitie='glasvezelversterkt polyesterhars',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/glasvezelversterkt-polyesterhars'),
        'ter-plaatse-gestort-beton': KeuzelijstWaarde(invulwaarde='ter-plaatse-gestort-beton',
                                                      label='ter plaatse gestort beton',
                                                      status='ingebruik',
                                                      definitie='ter plaatse gestort beton',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/ter-plaatse-gestort-beton')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

