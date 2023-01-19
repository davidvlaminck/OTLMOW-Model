# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeBrugligger(KeuzelijstField):
    """Het type van de brugligger."""
    naam = 'KlTypeBrugligger'
    label = 'Type brugligger'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeBrugligger'
    definition = 'Het type van de brugligger.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeBrugligger'
    options = {
        'dwarsdrager': KeuzelijstWaarde(invulwaarde='dwarsdrager',
                                        label='Dwarsdrager',
                                        status='ingebruik',
                                        definitie='Dragende dwarsbalk.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugligger/dwarsdrager'),
        'hoofdligger': KeuzelijstWaarde(invulwaarde='hoofdligger',
                                        label='Hoofdligger',
                                        status='ingebruik',
                                        definitie='Hoofdconstructiedeel van een brug, aan weerskanten van de te overspannen rivier of weg opgelegd en onderling verbonden tot een stijf geheel door zogenaamd windkruizen.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugligger/hoofdligger'),
        'langsligger': KeuzelijstWaarde(invulwaarde='langsligger',
                                        label='Langsligger',
                                        status='ingebruik',
                                        definitie='Balk volgens de lengterichting van de brug, waarop de eigenlijke rijvloer direct komt te dragen.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeBrugligger/langsligger')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

