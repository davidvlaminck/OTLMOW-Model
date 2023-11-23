# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeMicropaal(KeuzelijstField):
    """De soort van de micropaal."""
    naam = 'KlTypeMicropaal'
    label = 'Type micropaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeMicropaal'
    definition = 'De soort van de micropaal.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeMicropaal'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='Andere',
                                   status='ingebruik',
                                   definitie='Een ander type van micropaal. Details zijn terug te vinden in de technische fiche.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeMicropaal/andere'),
        'pds': KeuzelijstWaarde(invulwaarde='pds',
                                label='PDS',
                                status='ingebruik',
                                definitie='Micropaal vervaardigd door Penen Drilling System (PDS).',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeMicropaal/pds'),
        'titan': KeuzelijstWaarde(invulwaarde='titan',
                                  label='Titan',
                                  status='ingebruik',
                                  definitie='Micropaal vervaardigd door Ischebeck TITAN.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeMicropaal/titan')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

