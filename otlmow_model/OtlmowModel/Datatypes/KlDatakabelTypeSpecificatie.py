# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDatakabelTypeSpecificatie(KeuzelijstField):
    """Een verdere specificatie van het type van de datakabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
    naam = 'KlDatakabelTypeSpecificatie'
    label = 'Datakabel type specificatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDatakabelTypeSpecificatie'
    definition = 'Een verdere specificatie van het type van de datakabel volgens een vaste lijst om bv. de brandklasse mee te geven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDatakabelTypeSpecificatie'
    options = {
        'fr2': KeuzelijstWaarde(invulwaarde='fr2',
                                label='FR2',
                                status='ingebruik',
                                definitie='FR2',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelTypeSpecificatie/fr2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

