# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIOSignaaltype(KeuzelijstField):
    """Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal."""
    naam = 'KlIOSignaaltype'
    label = 'IO-kaart signaaltype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIOSignaaltype'
    definition = 'Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIOSignaaltype'
    options = {
        'analoog': KeuzelijstWaarde(invulwaarde='analoog',
                                    label='analoog',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOSignaaltype/analoog'),
        'digitaal': KeuzelijstWaarde(invulwaarde='digitaal',
                                     label='digitaal',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIOSignaaltype/digitaal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

