# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPompGroepMerk(KeuzelijstField):
    """De merknaam van de pompgoep."""
    naam = 'KlPompGroepMerk'
    label = 'Pompgroep merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPompGroepMerk'
    definition = 'De merknaam van de pompgoep.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPompGroepMerk'
    options: MappingProxyType[str, KeuzelijstWaarde] = MappingProxyType({
        'homa': KeuzelijstWaarde(invulwaarde='homa',
                                 label='HOMA',
                                 status='ingebruik',
                                 definitie='HOMA',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPompGroepMerk/homa')
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

