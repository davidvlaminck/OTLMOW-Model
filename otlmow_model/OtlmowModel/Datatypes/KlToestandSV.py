# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToestandSV(KeuzelijstField):
    """"""
    naam = 'KlToestandSV'
    label = ''
    objectUri = 'https://data.vlaanderen.be/ns/projecten#KlToestandSV'
    definition = ''
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToestandSV'
    options = {
        'in-gebruik': KeuzelijstWaarde(invulwaarde='in-gebruik',
                                       label='in gebruik',
                                       status='ingebruik',
                                       definitie='Het object vervult zijn functie.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToestandSV/in-gebruik'),
        'uit-gebruik': KeuzelijstWaarde(invulwaarde='uit-gebruik',
                                        label='uit gebruik',
                                        status='ingebruik',
                                        definitie='Het object vervult geen functie (meer) en is fysiek (deels) nog/al aanwezig op het terrein.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToestandSV/uit-gebruik'),
        'verwijderd': KeuzelijstWaarde(invulwaarde='verwijderd',
                                       label='verwijderd',
                                       status='ingebruik',
                                       definitie='Het object vervult geen functie meer en is fysiek niet meer aanwezig op het terrein.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToestandSV/verwijderd')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

