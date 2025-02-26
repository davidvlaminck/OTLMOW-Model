# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDrukknopMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Drukknop."""
    naam = 'KlDrukknopMerk'
    label = 'Drukknop merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDrukknopMerk'
    definition = 'Keuzelijst met merknamen voor Drukknop.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDrukknopMerk'
    options = {
        'eao': KeuzelijstWaarde(invulwaarde='eao',
                                label='EAO',
                                status='ingebruik',
                                definitie='EAO',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopMerk/eao'),
        'prisma': KeuzelijstWaarde(invulwaarde='prisma',
                                   label='Prisma',
                                   status='ingebruik',
                                   definitie='Prisma',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopMerk/prisma')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

