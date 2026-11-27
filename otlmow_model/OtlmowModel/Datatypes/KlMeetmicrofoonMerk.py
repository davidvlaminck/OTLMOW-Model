# coding=utf-8
from types import MappingProxyType

from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeetmicrofoonMerk(KeuzelijstField):
    """Het merk van de meetmicrofoon."""
    naam = 'KlMeetmicrofoonMerk'
    label = 'Meetmicrofoon merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetmicrofoonMerk'
    definition = 'Het merk van de meetmicrofoon.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetmicrofoonMerk'
    options: MappingProxyType[str, KeuzelijstWaarde] = MappingProxyType({
        'commend': KeuzelijstWaarde(invulwaarde='commend',
                                    label='Commend',
                                    status='ingebruik',
                                    definitie='Commend',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetmicrofoonMerk/commend')
    })

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

