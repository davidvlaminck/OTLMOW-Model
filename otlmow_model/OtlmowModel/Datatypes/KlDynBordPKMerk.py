# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordPKMerk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van Pijl-Kruisborden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlDynBordPKMerk'
    label = 'Dyn bord PK merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordPKMerk'
    definition = 'Keuzelijst met de gangbare merken van Pijl-Kruisborden. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordPKMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

