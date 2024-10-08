# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlooibakenType(KeuzelijstField):
    """vormen van een plooibaken."""
    naam = 'KlPlooibakenType'
    label = 'Plooibaken type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlooibakenType'
    definition = 'vormen van een plooibaken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlooibakenType'
    options = {
        'plooibaken-diameter-130-mm---M24': KeuzelijstWaarde(invulwaarde='plooibaken-diameter-130-mm---M24',
                                                             label='plooibaken diameter 130 mm - M24',
                                                             status='ingebruik',
                                                             definitie='Plooibaken diameter 130 mm – M24',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/plooibaken-diameter-130-mm---M24'),
        'plooibaken-diameter-80-mm---M16': KeuzelijstWaarde(invulwaarde='plooibaken-diameter-80-mm---M16',
                                                            label='plooibaken diameter 80 mm - M16',
                                                            status='ingebruik',
                                                            definitie='Plooibaken diameter 80 mm – M16',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/plooibaken-diameter-80-mm---M16'),
        'plooibaken-diameter-80-mm---M24': KeuzelijstWaarde(invulwaarde='plooibaken-diameter-80-mm---M24',
                                                            label='plooibaken diameter 80 mm - M24',
                                                            status='ingebruik',
                                                            definitie='Plooibaken diameter 80 mm – M24',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/plooibaken-diameter-80-mm---M24'),
        'verkeerszuil': KeuzelijstWaarde(invulwaarde='verkeerszuil',
                                         label='verkeerszuil',
                                         status='ingebruik',
                                         definitie='Verkeerszuil',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlooibakenType/verkeerszuil')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

