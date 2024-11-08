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
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSModelnaam/RVMS-12F05'),
        'vms-g1-rgb-112-144s': KeuzelijstWaarde(invulwaarde='vms-g1-rgb-112-144s',
                                                label='VMS.G1.RGB.112.144S',
                                                status='ingebruik',
                                                definitie='VMS.G1.RGB.112.144S',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSModelnaam/vms-g1-rgb-112-144s'),
        'vms-g1-rgb-96-64s': KeuzelijstWaarde(invulwaarde='vms-g1-rgb-96-64s',
                                              label='VMS.G1.RGB.96.64S',
                                              status='ingebruik',
                                              definitie='VMS.G1.RGB.96.64S',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSModelnaam/vms-g1-rgb-96-64s'),
        'vms1-f-4140x3230-3g-rb-ecofc2': KeuzelijstWaarde(invulwaarde='vms1-f-4140x3230-3g-rb-ecofc2',
                                                          label='VMS1.F.4140x3230.3G.RB.ECOFC2',
                                                          status='ingebruik',
                                                          definitie='VMS1-F-4140x3230-3G-RB-ECOFC2',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSModelnaam/vms1-f-4140x3230-3g-rb-ecofc2')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

