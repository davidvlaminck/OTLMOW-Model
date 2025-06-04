# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDunneOverlagingType(KeuzelijstField):
    """Types van dunne overlaging."""
    naam = 'KlDunneOverlagingType'
    label = 'Dunne overlaging type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDunneOverlagingType'
    definition = 'Types van dunne overlaging.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDunneOverlagingType'
    options = {
        'SME-D1': KeuzelijstWaarde(invulwaarde='SME-D1',
                                   label='SME-D1',
                                   status='ingebruik',
                                   definitie='SME-D1',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/SME-D1'),
        'SME-D2': KeuzelijstWaarde(invulwaarde='SME-D2',
                                   label='SME-D2',
                                   status='ingebruik',
                                   definitie='SME-D2',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/SME-D2'),
        'antisliplaag': KeuzelijstWaarde(invulwaarde='antisliplaag',
                                         label='antisliplaag',
                                         status='ingebruik',
                                         definitie='antisliplaag',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/antisliplaag'),
        'waterdichte-toplaag-met-instrooi-ng': KeuzelijstWaarde(invulwaarde='waterdichte-toplaag-met-instrooi-ng',
                                                                label='waterdichte toplaag met instrooiïng',
                                                                status='ingebruik',
                                                                definitie='De waterdichte toplaag is een meerlaags vloeibaar aangebracht systeem om de drager (beton, staal, ...) te beschermen tegen waterinfiltratie waarbij de 2de laag wordt ingestrooid met instrooimateriaal om stroefheid te verkrijgen.',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/waterdichte-toplaag-met-instrooi-ng'),
        'waterdichte-toplaag-zonder-instrooi-ng': KeuzelijstWaarde(invulwaarde='waterdichte-toplaag-zonder-instrooi-ng',
                                                                   label='waterdichte toplaag zonder instrooiïng',
                                                                   status='ingebruik',
                                                                   definitie='De waterdichte toplaag is een meerlaags vloeibaar aangebracht systeem om de drager (beton, staal, ...) te beschermen tegen waterinfiltratie.',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/waterdichte-toplaag-zonder-instrooi-ng')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

