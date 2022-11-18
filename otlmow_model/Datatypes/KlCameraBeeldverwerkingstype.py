# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCameraBeeldverwerkingstype(KeuzelijstField):
    """Lijst met mogelijke types van beeldverwerking eigen aan een camera (in tegenstelling tot beeldverwerking door andere assets)."""
    naam = 'KlCameraBeeldverwerkingstype'
    label = 'Camera beeldverwerkingstypes'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCameraBeeldverwerkingstype'
    definition = 'Lijst met mogelijke types van beeldverwerking eigen aan een camera (in tegenstelling tot beeldverwerking door andere assets).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCameraBeeldverwerkingstype'
    options = {
        'adr': KeuzelijstWaarde(invulwaarde='adr',
                                label='ADR',
                                status='ingebruik',
                                definitie='Interne beeldverwerking van het type ADR (detectie van symbolen op vrachtvervoer die gevaarlijke ladingen aangeven volgens het ADR-verdrag).',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraBeeldverwerkingstype/adr'),
        'aid': KeuzelijstWaarde(invulwaarde='aid',
                                label='AID',
                                status='ingebruik',
                                definitie='Interne beeldverwerking van het type automatische incident detectie (AID).',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCameraBeeldverwerkingstype/aid')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

