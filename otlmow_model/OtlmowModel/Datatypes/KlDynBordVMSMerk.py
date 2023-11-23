# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordVMSMerk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van VMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlDynBordVMSMerk'
    label = 'Dyn bord VMS merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordVMSMerk'
    definition = 'Keuzelijst met de gangbare merken van VMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordVMSMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

