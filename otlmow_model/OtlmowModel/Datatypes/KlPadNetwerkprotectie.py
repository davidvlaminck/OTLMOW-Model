# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPadNetwerkprotectie(KeuzelijstField):
    """Lijst van referenties van paden die redundantie kunnen leveren aan een Pad."""
    naam = 'KlPadNetwerkprotectie'
    label = 'Pad netwerkprotectie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPadNetwerkprotectie'
    definition = 'Lijst van referenties van paden die redundantie kunnen leveren aan een Pad.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPadNetwerkprotectie'
    options = {
        'Customer': KeuzelijstWaarde(invulwaarde='Customer',
                                     label='Customer',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/Customer'),
        'LACP': KeuzelijstWaarde(invulwaarde='LACP',
                                 label='LACP',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/LACP'),
        'LCAS': KeuzelijstWaarde(invulwaarde='LCAS',
                                 label='LCAS',
                                 status='ingebruik',
                                 definitie='Link Capacity Adjustment Scheme (Enkel bij SDH)',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/LCAS'),
        'MPLS-TP': KeuzelijstWaarde(invulwaarde='MPLS-TP',
                                    label='MPLS-TP',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/MPLS-TP'),
        'MSSpring': KeuzelijstWaarde(invulwaarde='MSSpring',
                                     label='MSSpring',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/MSSpring'),
        'NULL': KeuzelijstWaarde(invulwaarde='NULL',
                                 label='NULL',
                                 status='ingebruik',
                                 definitie='geen systeembeveiliging',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/NULL'),
        'None': KeuzelijstWaarde(invulwaarde='None',
                                 label='None',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/None'),
        'OPS': KeuzelijstWaarde(invulwaarde='OPS',
                                label='OPS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/OPS'),
        'Other': KeuzelijstWaarde(invulwaarde='Other',
                                  label='Other',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/Other'),
        'SNCP': KeuzelijstWaarde(invulwaarde='SNCP',
                                 label='SNCP',
                                 status='ingebruik',
                                 definitie='Sub Network Connection Protection (Bij OTN en SDH)',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/SNCP'),
        'STP': KeuzelijstWaarde(invulwaarde='STP',
                                label='STP',
                                status='ingebruik',
                                definitie='Carrier Ethernet',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/STP')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

