# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordRVMSModelnaam(KeuzelijstField):
    """Keuzelijst met de gangbare modelnamen van RVMS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""
    naam = 'KlDynBordRVMSModelnaam'
    label = 'Dyn bord RVMS modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordRVMSModelnaam'
    definition = 'Keuzelijst met de gangbare modelnamen van RVMS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordRVMSModelnaam'
    options = {
        'RVMS-06I04': KeuzelijstWaarde(invulwaarde='RVMS-06I04',
                                       label='RVMS-06I04',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSModelnaam/RVMS-06I04'),
        'RVMS-12F05': KeuzelijstWaarde(invulwaarde='RVMS-12F05',
                                       label='RVMS-12F05',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSModelnaam/RVMS-12F05')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

