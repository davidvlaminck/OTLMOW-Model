# coding=utf-8
from ..BaseClasses.KeuzelijstField import KeuzelijstField
from ..BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlServicePrioriteit(KeuzelijstField):
    """Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden"""
    naam = 'KlServicePrioriteit'
    label = 'Serviceprioriteit'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlServicePrioriteit'
    definition = 'Het prioriteitsniveau dat aangeeft hoe dringend iets moet onderhouden/gerepareerd worden'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlServicePrioriteit'
    options = {
        'spitsstrook': KeuzelijstWaarde(invulwaarde='spitsstrook',
                                        label='spitsstrook',
                                        status='ingebruik',
                                        definitie='Geeft aan dat de camera een rol speelt bij de monitoring of controle van een spitsstrook en impliceert dat er een hogere prioriteit nodig is voor opvolging van storingen of interventies, gezien de directe impact op verkeersveiligheid en doorstroming.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlServicePrioriteit/spitsstrook')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

