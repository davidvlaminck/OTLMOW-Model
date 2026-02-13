# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


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
                                        definitie='BM Technics',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangspoortMerk/bm-technics'),
        'hormann': KeuzelijstWaarde(invulwaarde='hormann',
                                    label='Hormann',
                                    status='ingebruik',
                                    definitie='Hormann',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangspoortMerk/hormann'),
        'segaf': KeuzelijstWaarde(invulwaarde='segaf',
                                  label='Segaf',
                                  status='ingebruik',
                                  definitie='Segaf',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlToegangspoortMerk/segaf')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

