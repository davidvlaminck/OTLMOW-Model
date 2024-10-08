# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTelecomkabelTypeSpecificatie(KeuzelijstField):
    """Lijst met mogelijke specificaties van het type van de telecomkabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
    naam = 'KlTelecomkabelTypeSpecificatie'
    label = 'Telecomkabel type specificatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTelecomkabelTypeSpecificatie'
    definition = 'Lijst met mogelijke specificaties van het type van de telecomkabel volgens een vaste lijst om bv. de brandklasse mee te geven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTelecomkabelTypeSpecificatie'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

