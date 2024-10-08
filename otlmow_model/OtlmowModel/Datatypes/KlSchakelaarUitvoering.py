# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchakelaarUitvoering(KeuzelijstField):
    """Keuzelijst voor de uitvoering van een schakelaar."""
    naam = 'KlSchakelaarUitvoering'
    label = 'Uitvoering schakelaar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSchakelaarUitvoering'
    definition = 'Keuzelijst voor de uitvoering van een schakelaar.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchakelaarUitvoering'
    options = {
        'binaire-draaischakelaar': KeuzelijstWaarde(invulwaarde='binaire-draaischakelaar',
                                                    label='binaire draaischakelaar',
                                                    status='ingebruik',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchakelaarUitvoering/binaire-draaischakelaar'),
        'klikschakelaar': KeuzelijstWaarde(invulwaarde='klikschakelaar',
                                           label='klikschakelaar',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchakelaarUitvoering/klikschakelaar'),
        'niet-gespecificeerd': KeuzelijstWaarde(invulwaarde='niet-gespecificeerd',
                                                label='niet gespecificeerd',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchakelaarUitvoering/niet-gespecificeerd'),
        'schuifschakelaar': KeuzelijstWaarde(invulwaarde='schuifschakelaar',
                                             label='schuifschakelaar',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchakelaarUitvoering/schuifschakelaar'),
        'sleutelschakelaar': KeuzelijstWaarde(invulwaarde='sleutelschakelaar',
                                              label='sleutelschakelaar',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchakelaarUitvoering/sleutelschakelaar'),
        'standenschakelaar': KeuzelijstWaarde(invulwaarde='standenschakelaar',
                                              label='standenschakelaar',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchakelaarUitvoering/standenschakelaar'),
        'trekschakelaar': KeuzelijstWaarde(invulwaarde='trekschakelaar',
                                           label='trekschakelaar',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchakelaarUitvoering/trekschakelaar')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

