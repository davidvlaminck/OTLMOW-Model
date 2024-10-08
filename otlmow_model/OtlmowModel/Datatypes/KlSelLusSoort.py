# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSelLusSoort(KeuzelijstField):
    """Keuzelijst met verschillende soorten selectieve lussen."""
    naam = 'KlSelLusSoort'
    label = 'Selectieve lus soort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSelLusSoort'
    definition = 'Keuzelijst met verschillende soorten selectieve lussen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSelLusSoort'
    options = {
        'buslus': KeuzelijstWaarde(invulwaarde='buslus',
                                   label='buslus',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/buslus'),
        'trambuslus': KeuzelijstWaarde(invulwaarde='trambuslus',
                                       label='trambuslus',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/trambuslus'),
        'trambuslus-virtueel': KeuzelijstWaarde(invulwaarde='trambuslus-virtueel',
                                                label='trambuslus virtueel',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/trambuslus-virtueel'),
        'tramlus': KeuzelijstWaarde(invulwaarde='tramlus',
                                    label='tramlus',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus'),
        'tramlus-magnetisch': KeuzelijstWaarde(invulwaarde='tramlus-magnetisch',
                                               label='tramlus magnetisch',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus-magnetisch'),
        'tramlus-virtueel': KeuzelijstWaarde(invulwaarde='tramlus-virtueel',
                                             label='tramlus virtueel',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus-virtueel'),
        'tramlus-wisselcontact-DeLijn': KeuzelijstWaarde(invulwaarde='tramlus-wisselcontact-DeLijn',
                                                         label='tramlus wisselcontact DeLijn',
                                                         status='ingebruik',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus-wisselcontact-DeLijn')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

