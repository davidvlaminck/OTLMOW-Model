# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVirtueleServerMerk(KeuzelijstField):
    """Het merk van de virtuele server."""
    naam = 'KlVirtueleServerMerk'
    label = 'Virtuele server merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVirtueleServerMerk'
    definition = 'Het merk van de virtuele server.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVirtueleServerMerk'
    options = {
        'dell': KeuzelijstWaarde(invulwaarde='dell',
                                 label='Dell',
                                 status='ingebruik',
                                 definitie='Dell',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVirtueleServerMerk/dell'),
        'hp': KeuzelijstWaarde(invulwaarde='hp',
                               label='HP',
                               status='ingebruik',
                               definitie='HP',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVirtueleServerMerk/hp'),
        'peek': KeuzelijstWaarde(invulwaarde='peek',
                                 label='Peek',
                                 status='ingebruik',
                                 definitie='Peek.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVirtueleServerMerk/peek'),
        'ram': KeuzelijstWaarde(invulwaarde='ram',
                                label='RAM',
                                status='ingebruik',
                                definitie='RAM',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVirtueleServerMerk/ram')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

