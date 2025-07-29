# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOptischeWegdeksensorModelnaam(KeuzelijstField):
    """Optische wegdeksensor modelnamen."""
    naam = 'KlOptischeWegdeksensorModelnaam'
    label = 'Optische wegdeksensor modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOptischeWegdeksensorModelnaam'
    definition = 'Optische wegdeksensor modelnamen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOptischeWegdeksensorModelnaam'
    options = {
        'dsc111': KeuzelijstWaarde(invulwaarde='dsc111',
                                   label='DSC111',
                                   status='ingebruik',
                                   definitie='DSC111',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOptischeWegdeksensorModelnaam/dsc111'),
        'dsc211': KeuzelijstWaarde(invulwaarde='dsc211',
                                   label='DSC211',
                                   status='ingebruik',
                                   definitie='DSC211',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOptischeWegdeksensorModelnaam/dsc211'),
        'dst111': KeuzelijstWaarde(invulwaarde='dst111',
                                   label='DST111',
                                   status='ingebruik',
                                   definitie='DST111',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOptischeWegdeksensorModelnaam/dst111')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

