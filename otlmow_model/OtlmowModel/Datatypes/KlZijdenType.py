# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZijdenType(KeuzelijstField):
    """Het type van de zijden."""
    naam = 'KlZijdenType'
    label = 'Zijden type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlZijdenType'
    definition = 'Het type van de zijden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZijdenType'
    options = {
        'gebogen': KeuzelijstWaarde(invulwaarde='gebogen',
                                    label='Gebogen',
                                    status='ingebruik',
                                    definitie='Gebogen zijden.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZijdenType/gebogen'),
        'rechte': KeuzelijstWaarde(invulwaarde='rechte',
                                   label='Rechte',
                                   status='ingebruik',
                                   definitie='Rechte zijden.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZijdenType/rechte'),
        'rechte-en-schuine': KeuzelijstWaarde(invulwaarde='rechte-en-schuine',
                                              label='Rechte en schuine',
                                              status='ingebruik',
                                              definitie='Rechte en schuine zijden gecombineerd.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZijdenType/rechte-en-schuine'),
        'ronde': KeuzelijstWaarde(invulwaarde='ronde',
                                  label='Ronde',
                                  status='ingebruik',
                                  definitie='Ronde zijden.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZijdenType/ronde'),
        'schuine': KeuzelijstWaarde(invulwaarde='schuine',
                                    label='Schuine',
                                    status='ingebruik',
                                    definitie='Schuine zijden.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZijdenType/schuine')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

