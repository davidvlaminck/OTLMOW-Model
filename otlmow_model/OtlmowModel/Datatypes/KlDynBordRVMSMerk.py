# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordRVMSMerk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van RVMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlDynBordRVMSMerk'
    label = 'Dyn bord RVMS merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordRVMSMerk'
    definition = 'Keuzelijst met de gangbare merken van RVMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordRVMSMerk'
    options = {
        'dms': KeuzelijstWaarde(invulwaarde='dms',
                                label='DMS',
                                status='ingebruik',
                                definitie='DMS',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSMerk/dms'),
        'swarco': KeuzelijstWaarde(invulwaarde='swarco',
                                   label='Swarco',
                                   status='ingebruik',
                                   definitie='Swarco',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSMerk/swarco')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

