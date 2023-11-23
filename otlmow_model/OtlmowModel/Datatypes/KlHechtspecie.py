# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHechtspecie(KeuzelijstField):
    """Keuzelijst met hecht specie van gestapelde ruwe steen."""
    naam = 'KlHechtspecie'
    label = 'Hecht specie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHechtspecie'
    definition = 'Keuzelijst met hecht specie van gestapelde ruwe steen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHechtspecie'
    options = {
        'gebiedseigen-grond': KeuzelijstWaarde(invulwaarde='gebiedseigen-grond',
                                               label='gebiedseigen grond',
                                               status='ingebruik',
                                               definitie='gebiedseigen grond',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHechtspecie/gebiedseigen-grond'),
        'zandcement': KeuzelijstWaarde(invulwaarde='zandcement',
                                       label='zandcement',
                                       status='ingebruik',
                                       definitie='zandcement',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHechtspecie/zandcement')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

