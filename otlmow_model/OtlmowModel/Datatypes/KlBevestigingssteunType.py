# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBevestigingssteunType(KeuzelijstField):
    """De mogelijk types van een bevestigingssteun."""
    naam = 'KlBevestigingssteunType'
    label = 'Bevestigingssteun type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBevestigingssteunType'
    definition = 'De mogelijk types van een bevestigingssteun.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBevestigingssteunType'
    options = {
        'baar': KeuzelijstWaarde(invulwaarde='baar',
                                 label='baar',
                                 status='ingebruik',
                                 definitie='Een staaf waaraan bv. een antenne kan worden bevestigd.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBevestigingssteunType/baar')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

