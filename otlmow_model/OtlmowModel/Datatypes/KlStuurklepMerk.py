# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStuurklepMerk(KeuzelijstField):
    """Merknamen van een stuurklep."""
    naam = 'KlStuurklepMerk'
    label = 'Stuurklep merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStuurklepMerk'
    definition = 'Merknamen van een stuurklep.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStuurklepMerk'
    options = {
        'avk': KeuzelijstWaarde(invulwaarde='avk',
                                label='AVK',
                                status='ingebruik',
                                definitie='AVK',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStuurklepMerk/avk'),
        'eriks': KeuzelijstWaarde(invulwaarde='eriks',
                                  label='Eriks',
                                  status='ingebruik',
                                  definitie='Eriks',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStuurklepMerk/eriks'),
        'genebre': KeuzelijstWaarde(invulwaarde='genebre',
                                    label='Genebre',
                                    status='ingebruik',
                                    definitie='Genebre',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStuurklepMerk/genebre')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

