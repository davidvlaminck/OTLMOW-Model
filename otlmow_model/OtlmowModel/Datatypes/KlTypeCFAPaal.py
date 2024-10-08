# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeCFAPaal(KeuzelijstField):
    """De soort van de CFA-paal."""
    naam = 'KlTypeCFAPaal'
    label = 'Type CFA-paal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeCFAPaal'
    definition = 'De soort van de CFA-paal.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeCFAPaal'
    options = {
        'met-beperkte-grondverdringing-beperkte-grondontspanning': KeuzelijstWaarde(invulwaarde='met-beperkte-grondverdringing-beperkte-grondontspanning',
                                                                                    label='Met beperkte grondverdringing/beperkte grondontspanning',
                                                                                    status='ingebruik',
                                                                                    definitie='CFA-paal met speciale voorzieningen om grondontspanning te voorkomen.',
                                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeCFAPaal/met-beperkte-grondverdringing-beperkte-grondontspanning'),
        'met-uitgraving-van-de-grond-grondontspanning': KeuzelijstWaarde(invulwaarde='met-uitgraving-van-de-grond-grondontspanning',
                                                                         label='Met uitgraving van de grond (grondontspanning)',
                                                                         status='ingebruik',
                                                                         definitie='CFA-paal zonder speciale voorzieningen om grondontspanning te voorkomen.',
                                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeCFAPaal/met-uitgraving-van-de-grond-grondontspanning')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

