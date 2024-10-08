# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPompKamerFunctie(KeuzelijstField):
    """De mogelijke functies die een pompkamer kan invullen."""
    naam = 'KlPompKamerFunctie'
    label = 'Kamer functie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPompKamerFunctie'
    definition = 'De mogelijke functies die een pompkamer kan invullen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPompKamerFunctie'
    options = {
        'natte-pompkelder': KeuzelijstWaarde(invulwaarde='natte-pompkelder',
                                             label='natte pompkelder',
                                             status='ingebruik',
                                             definitie='Een kamer waarin de op te pompen vloeistof verzameld wordt.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompKamerFunctie/natte-pompkelder'),
        'slibvang': KeuzelijstWaarde(invulwaarde='slibvang',
                                     label='slibvang',
                                     status='ingebruik',
                                     definitie='Een kamer waarin deeltjes zwaarder dan water kunnen bezinken zodat die niet in de natte pompkelder terecht komen.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompKamerFunctie/slibvang')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

