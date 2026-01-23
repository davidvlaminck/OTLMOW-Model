# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAudioversterkerModelnaam(KeuzelijstField):
    """De modelnaam van de audioversterker."""
    naam = 'KlAudioversterkerModelnaam'
    label = 'Audioversterker modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAudioversterkerModelnaam'
    definition = 'De modelnaam van de audioversterker.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAudioversterkerModelnaam'
    options = {
        'industryamp-pb-800-dn': KeuzelijstWaarde(invulwaarde='industryamp-pb-800-dn',
                                                  label='IndustryAmp PB-800-DN',
                                                  status='ingebruik',
                                                  definitie='IndustryAmp PB-800-DN',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAudioversterkerModelnaam/industryamp-pb-800-dn')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

