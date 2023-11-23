# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangspoortMerk(KeuzelijstField):
    """Lijst met merknamen voor allerlei types van toegangspoorten volgens de fabrikant"""
    naam = 'KlToegangspoortMerk'
    label = 'Toegangspoort merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlToegangspoortMerk'
    definition = 'Lijst met merknamen voor allerlei types van toegangspoorten volgens de fabrikant'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangspoortMerk'
    options = {
        'bm-technics': KeuzelijstWaarde(invulwaarde='bm-technics',
                                        label='BM Technics',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangspoortMerk/bm-technics'),
        'hormann': KeuzelijstWaarde(invulwaarde='hormann',
                                    label='Hormann',
                                    status='ingebruik',
                                    definitie='HÃƒÂ¶rmann',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangspoortMerk/hormann')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

