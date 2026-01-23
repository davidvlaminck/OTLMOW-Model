# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPLCModelnaam(KeuzelijstField):
    """De modelnaam van de PLC."""
    naam = 'KlPLCModelnaam'
    label = 'PLC model'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPLCModelnaam'
    definition = 'De modelnaam van de PLC.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPLCModelnaam'
    options = {
        'axc-f-2152': KeuzelijstWaarde(invulwaarde='axc-f-2152',
                                       label='AXC-F-2152',
                                       status='ingebruik',
                                       definitie='AXC-F-2152',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/axc-f-2152'),
        'axc-f-3152': KeuzelijstWaarde(invulwaarde='axc-f-3152',
                                       label='AXC-F-3152',
                                       status='ingebruik',
                                       definitie='AXC-F-3152',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/axc-f-3152'),
        'dmf031': KeuzelijstWaarde(invulwaarde='dmf031',
                                   label='DMF031',
                                   status='ingebruik',
                                   definitie='DMF031',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/dmf031'),
        'dmf132': KeuzelijstWaarde(invulwaarde='dmf132',
                                   label='DMF132',
                                   status='ingebruik',
                                   definitie='DMF132',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/dmf132'),
        'dmf133': KeuzelijstWaarde(invulwaarde='dmf133',
                                   label='DMF133',
                                   status='ingebruik',
                                   definitie='DMF133',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/dmf133'),
        'dmu703': KeuzelijstWaarde(invulwaarde='dmu703',
                                   label='DMU703',
                                   status='ingebruik',
                                   definitie='DMU703',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/dmu703'),
        'lfc7630-02': KeuzelijstWaarde(invulwaarde='lfc7630-02',
                                       label='LFC7630-02',
                                       status='ingebruik',
                                       definitie='LFC7630-02',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/lfc7630-02'),
        's7-1200': KeuzelijstWaarde(invulwaarde='s7-1200',
                                    label='S7-1200',
                                    status='ingebruik',
                                    definitie='S7-1200',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPLCModelnaam/s7-1200')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

