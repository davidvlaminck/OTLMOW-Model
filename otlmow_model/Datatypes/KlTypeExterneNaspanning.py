# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeExterneNaspanning(KeuzelijstField):
    """Het type externe naspanning."""
    naam = 'KlTypeExterneNaspanning'
    label = 'Type externe naspanning'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeExterneNaspanning'
    definition = 'Het type externe naspanning.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeExterneNaspanning'
    options = {
        'voorspanning-met-aanhechting': KeuzelijstWaarde(invulwaarde='voorspanning-met-aanhechting',
                                                         label='Voorspanning met aanhechting',
                                                         status='ingebruik',
                                                         definitie='Bij voorspanning met aanhechting (VMA) worden de strengen in de omhullingsbuizen ingevoerd, aangespannen, verankerd en daarna worden de omhullingsbuizen geÃ¯njecteerd met een speciale cementmortel.',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeExterneNaspanning/voorspanning-met-aanhechting'),
        'voorspanning-zonder-aanhechting': KeuzelijstWaarde(invulwaarde='voorspanning-zonder-aanhechting',
                                                            label='Voorspanning zonder aanhechting',
                                                            status='ingebruik',
                                                            definitie='Bij voorspanning zonder aanhechting (VZA) zit elke streng van de kabel in een aparte polyethyleen-omhulling dewelke gevuld is met vet. Deze omhulde strengen worden ingevoerd in de omhullingsbuizen, daarna worden de omhullingsbuizen geÃ¯njecteerd met cementmortel en dan pas worden de strengen aangespannen en verankerd.',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeExterneNaspanning/voorspanning-zonder-aanhechting')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

