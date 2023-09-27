# coding=utf-8
import random
from otlmow_model.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelmofVerbinding(KeuzelijstField):
    """Lijst van mogelijke types van verbindigen die een kabelmof kan realiseren."""
    naam = 'KlKabelmofVerbinding'
    label = 'Kabelmof verbindingtypes'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelmofVerbinding'
    definition = 'Lijst van mogelijke types van verbindigen die een kabelmof kan realiseren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelmofVerbinding'
    options = {
        'doorverbinding': KeuzelijstWaarde(invulwaarde='doorverbinding',
                                           label='doorverbinding',
                                           status='ingebruik',
                                           definitie='doorverbinding',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmofVerbinding/doorverbinding'),
        'eindmof': KeuzelijstWaarde(invulwaarde='eindmof',
                                    label='eindmof',
                                    status='ingebruik',
                                    definitie='eindmof',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmofVerbinding/eindmof'),
        't-mof': KeuzelijstWaarde(invulwaarde='t-mof',
                                  label='T-mof',
                                  status='ingebruik',
                                  definitie='T-mof',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmofVerbinding/t-mof'),
        'y-mof': KeuzelijstWaarde(invulwaarde='y-mof',
                                  label='Y-mof',
                                  status='ingebruik',
                                  definitie='Y-mof',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmofVerbinding/y-mof')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

