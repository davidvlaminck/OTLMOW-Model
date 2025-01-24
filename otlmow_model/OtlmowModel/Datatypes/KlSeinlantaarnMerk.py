# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinlantaarnMerk(KeuzelijstField):
    """Keuzelijst met merknamen voor Seinlantaarn."""
    naam = 'KlSeinlantaarnMerk'
    label = 'seinlantaarn merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlSeinlantaarnMerk'
    definition = 'Keuzelijst met merknamen voor Seinlantaarn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinlantaarnMerk'
    options = {
        'swarco': KeuzelijstWaarde(invulwaarde='swarco',
                                   label='SWARCO',
                                   status='ingebruik',
                                   definitie='SWARCO',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinlantaarnMerk/swarco')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

