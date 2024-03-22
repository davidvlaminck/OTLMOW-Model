# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSegmentcontrollerMerk(KeuzelijstField):
    """De mogelijke merken voor een segmentcontroller."""
    naam = 'KlSegmentcontrollerMerk'
    label = 'Segmentcontroller merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSegmentcontrollerMerk'
    definition = 'De mogelijke merken voor een segmentcontroller.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSegmentcontrollerMerk'
    options = {
        'lacroix': KeuzelijstWaarde(invulwaarde='lacroix',
                                    label='Lacroix',
                                    status='ingebruik',
                                    definitie='Lacroix',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSegmentcontrollerMerk/lacroix'),
        'smartnodes': KeuzelijstWaarde(invulwaarde='smartnodes',
                                       label='SmartNodes',
                                       status='ingebruik',
                                       definitie='SmartNodes',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSegmentcontrollerMerk/smartnodes')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

