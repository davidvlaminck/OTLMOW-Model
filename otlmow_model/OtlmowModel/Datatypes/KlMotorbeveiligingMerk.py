# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMotorbeveiligingMerk(KeuzelijstField):
    """Lijst met merknamen voor motorbeveiligingen volgens de fabrikant.."""
    naam = 'KlMotorbeveiligingMerk'
    label = 'Merken  motorbeveiligingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMotorbeveiligingMerk'
    definition = 'Lijst met merknamen voor motorbeveiligingen volgens de fabrikant..'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMotorbeveiligingMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

