# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordExternePUMerk(KeuzelijstField):
    """Keuzelijst met merknamen van externe PUs."""
    naam = 'KlDynBordExternePUMerk'
    label = 'Keuzelijst met merknamen van externe PUs'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordExternePUMerk'
    definition = 'Keuzelijst met merknamen van externe PUs.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordExternePUMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

