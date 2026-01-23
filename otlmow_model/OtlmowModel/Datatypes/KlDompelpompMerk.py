# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDompelpompMerk(KeuzelijstField):
    """Lijst van merknamen van dompelpompen volgens de fabrikant."""
    naam = 'KlDompelpompMerk'
    label = 'Merknamen dompelpompen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDompelpompMerk'
    definition = 'Lijst van merknamen van dompelpompen volgens de fabrikant.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDompelpompMerk'
    options = {
        'homa': KeuzelijstWaarde(invulwaarde='homa',
                                 label='HOMA',
                                 status='ingebruik',
                                 definitie='HOMA',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDompelpompMerk/homa')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

