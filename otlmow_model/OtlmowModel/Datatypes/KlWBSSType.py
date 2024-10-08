# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWBSSType(KeuzelijstField):
    """Types van waterdoorlatende betonstraatstenen en betontegels."""
    naam = 'KlWBSSType'
    label = 'WBSS type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWBSSType'
    definition = 'Types van waterdoorlatende betonstraatstenen en betontegels.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWBSSType'
    options = {
        'gekleurde-met-anorganische-pigmenten': KeuzelijstWaarde(invulwaarde='gekleurde-met-anorganische-pigmenten',
                                                                 label='gekleurde met anorganische pigmenten',
                                                                 status='ingebruik',
                                                                 definitie='gekleurde waterdoorlatende betonstraatstenen met anorganische pigmenten',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/gekleurde-met-anorganische-pigmenten'),
        'gekleurde-met-kleurondersteunende-granulaten': KeuzelijstWaarde(invulwaarde='gekleurde-met-kleurondersteunende-granulaten',
                                                                         label='gekleurde met kleurondersteunende granulaten',
                                                                         status='ingebruik',
                                                                         definitie='gekleurde waterdoorlatende betonstraatstenen met kleurondersteunende granulaten',
                                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/gekleurde-met-kleurondersteunende-granulaten'),
        'grijze': KeuzelijstWaarde(invulwaarde='grijze',
                                   label='grijze',
                                   status='ingebruik',
                                   definitie='grijze waterdoorlatende betonstraatstenen',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/grijze'),
        'waterdoorlatende-betontegel': KeuzelijstWaarde(invulwaarde='waterdoorlatende-betontegel',
                                                        label='waterdoorlatende betontegel',
                                                        status='ingebruik',
                                                        definitie='waterdoorlatende betontegel',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/waterdoorlatende-betontegel'),
        'witte-met-kleurondersteunende-granulaten': KeuzelijstWaarde(invulwaarde='witte-met-kleurondersteunende-granulaten',
                                                                     label='witte met kleurondersteunende granulaten',
                                                                     status='ingebruik',
                                                                     definitie='witte waterdoorlatende betonstraatstenen met kleurondersteunende granulaten',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWBSSType/witte-met-kleurondersteunende-granulaten')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

