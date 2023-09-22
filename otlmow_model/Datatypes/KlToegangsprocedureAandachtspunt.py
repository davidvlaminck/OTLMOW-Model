# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlToegangsprocedureAandachtspunt(KeuzelijstField):
    """De soorten aandachtspunten voor toegang tot een object."""
    naam = 'KlToegangsprocedureAandachtspunt'
    label = 'Toegangsprocedure aandachtspunt'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlToegangsprocedureAandachtspunt'
    definition = 'De soorten aandachtspunten voor toegang tot een object.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlToegangsprocedureAandachtspunt'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

