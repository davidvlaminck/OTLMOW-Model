# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRetroreflecterendVerkeersbordMerk(KeuzelijstField):
    """Keuzelijst met merknamen van retroreflecterende verkeersborden. De merknaam duidt op de leverancier of producent van het verkeersbord."""
    naam = 'KlRetroreflecterendVerkeersbordMerk'
    label = 'Retroreflecterend Verkeersbord Merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRetroreflecterendVerkeersbordMerk'
    definition = 'Keuzelijst met merknamen van retroreflecterende verkeersborden. De merknaam duidt op de leverancier of producent van het verkeersbord.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRetroreflecterendVerkeersbordMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

