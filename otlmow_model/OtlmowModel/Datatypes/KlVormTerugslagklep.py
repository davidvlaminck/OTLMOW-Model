# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVormTerugslagklep(KeuzelijstField):
    """De vorm van opening van de terugslagklep."""
    naam = 'KlVormTerugslagklep'
    label = 'Vorm terugslagklep'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormTerugslagklep'
    definition = 'De vorm van opening van de terugslagklep.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormTerugslagklep'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   definitie='andere',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/andere'),
        'circkelvormig': KeuzelijstWaarde(invulwaarde='circkelvormig',
                                          label='circkelvormig',
                                          status='ingebruik',
                                          definitie='circkelvormig',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/circkelvormig'),
        'rechthoekig': KeuzelijstWaarde(invulwaarde='rechthoekig',
                                        label='rechthoekig',
                                        status='ingebruik',
                                        definitie='rechthoekig',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/rechthoekig')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

