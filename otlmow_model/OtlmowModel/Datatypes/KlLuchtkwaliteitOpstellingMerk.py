# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLuchtkwaliteitOpstellingMerk(KeuzelijstField):
    """Het merk van een onderdeel uit een luchtkwaliteitsinstallatie."""
    naam = 'KlLuchtkwaliteitOpstellingMerk'
    label = 'Luchtkwaliteitsopstelling merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlLuchtkwaliteitOpstellingMerk'
    definition = 'Het merk van een onderdeel uit een luchtkwaliteitsinstallatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLuchtkwaliteitOpstellingMerk'
    options = {
        'sick': KeuzelijstWaarde(invulwaarde='sick',
                                 label='sick',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuchtkwaliteitOpstellingMerk/sick')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

