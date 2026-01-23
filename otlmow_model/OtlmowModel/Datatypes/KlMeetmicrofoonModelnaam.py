# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeetmicrofoonModelnaam(KeuzelijstField):
    """De modelnaam van de meetmicrofoon."""
    naam = 'KlMeetmicrofoonModelnaam'
    label = 'Meetmicrofoon modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetmicrofoonModelnaam'
    definition = 'De modelnaam van de meetmicrofoon.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetmicrofoonModelnaam'
    options = {
        'ws200pi': KeuzelijstWaarde(invulwaarde='ws200pi',
                                    label='WS200PI',
                                    status='ingebruik',
                                    definitie='WS200PI',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetmicrofoonModelnaam/ws200pi')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

