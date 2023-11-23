# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


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
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

