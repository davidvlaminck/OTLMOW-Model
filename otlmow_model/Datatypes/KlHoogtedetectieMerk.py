# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHoogtedetectieMerk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van hoogtedetectiesystemen. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlHoogtedetectieMerk'
    label = 'Hoogtedetectie merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHoogtedetectieMerk'
    definition = 'Keuzelijst met de gangbare merken van hoogtedetectiesystemen. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHoogtedetectieMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

