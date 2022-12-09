# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTelecomCableMateriaalType(KeuzelijstField):
    """Codelijst met waardes voor het type materiaal van een telecomkabel."""
    naam = 'KlTelecomCableMateriaalType'
    label = 'Datakabel materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTelecomCableMateriaalType'
    definition = 'Codelijst met waardes voor het type materiaal van een telecomkabel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTelecomCableMateriaalType'
    options = {
        'coaxial': KeuzelijstWaarde(invulwaarde='coaxial',
                                    label='coaxial',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/coaxial'),
        'ftp': KeuzelijstWaarde(invulwaarde='ftp',
                                label='FTP',
                                status='verwijderd',
                                definitie='FTP',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/ftp'),
        'opticalfiber': KeuzelijstWaarde(invulwaarde='opticalfiber',
                                         label='opticalFiber',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/opticalfiber'),
        'other': KeuzelijstWaarde(invulwaarde='other',
                                  label='other',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/other'),
        'sty-sy': KeuzelijstWaarde(invulwaarde='sty-sy',
                                   label='STY SY',
                                   status='verwijderd',
                                   definitie='STY SY',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/sty-sy'),
        'tvavb': KeuzelijstWaarde(invulwaarde='tvavb',
                                  label='TVAVB',
                                  status='verwijderd',
                                  definitie='TVAVB',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/tvavb'),
        'twistedpair': KeuzelijstWaarde(invulwaarde='twistedpair',
                                        label='twistedPair',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/twistedpair'),
        'vvt': KeuzelijstWaarde(invulwaarde='vvt',
                                label='VVT',
                                status='verwijderd',
                                definitie='VVT',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/vvt')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

