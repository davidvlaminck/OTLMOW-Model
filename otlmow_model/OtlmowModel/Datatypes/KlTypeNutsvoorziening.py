# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeNutsvoorziening(KeuzelijstField):
    """Het type nutsvoorziening van een straatkap verwijst naar de specifieke aard van de nutsinfrastructuur waartoe het deksel toegang biedt."""
    naam = 'KlTypeNutsvoorziening'
    label = 'Keuzelijst type nutsvoorziening'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTypeNutsvoorziening'
    definition = 'Het type nutsvoorziening van een straatkap verwijst naar de specifieke aard van de nutsinfrastructuur waartoe het deksel toegang biedt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeNutsvoorziening'
    options = {
        'brandkraan': KeuzelijstWaarde(invulwaarde='brandkraan',
                                       label='brandkraan',
                                       status='ingebruik',
                                       definitie='brandkraan',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeNutsvoorziening/brandkraan'),
        'elektriciteit': KeuzelijstWaarde(invulwaarde='elektriciteit',
                                          label='elektriciteit',
                                          status='ingebruik',
                                          definitie='elektriciteit',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeNutsvoorziening/elektriciteit'),
        'gas': KeuzelijstWaarde(invulwaarde='gas',
                                label='gas',
                                status='ingebruik',
                                definitie='gas',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeNutsvoorziening/gas'),
        'telecom': KeuzelijstWaarde(invulwaarde='telecom',
                                    label='telecom',
                                    status='ingebruik',
                                    definitie='telecom',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeNutsvoorziening/telecom'),
        'water': KeuzelijstWaarde(invulwaarde='water',
                                  label='water',
                                  status='ingebruik',
                                  definitie='water',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeNutsvoorziening/water')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

