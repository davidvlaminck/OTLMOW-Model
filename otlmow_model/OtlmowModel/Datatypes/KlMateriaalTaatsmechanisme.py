# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMateriaalTaatsmechanisme(KeuzelijstField):
    """Lijst met de verschillende materialen van een taatsmechanisme."""
    naam = 'KlMateriaalTaatsmechanisme'
    label = 'Materiaal taatsmechanisme'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalTaatsmechanisme'
    definition = 'Lijst met de verschillende materialen van een taatsmechanisme.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalTaatsmechanisme'
    options = {
        'gietstaal': KeuzelijstWaarde(invulwaarde='gietstaal',
                                      label='gietstaal',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTaatsmechanisme/gietstaal'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='rvs',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTaatsmechanisme/rvs'),
        'smeedstaal': KeuzelijstWaarde(invulwaarde='smeedstaal',
                                       label='smeedstaal',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTaatsmechanisme/smeedstaal'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalTaatsmechanisme/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

