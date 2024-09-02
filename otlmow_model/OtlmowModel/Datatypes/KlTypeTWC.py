# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTypeTWC(KeuzelijstField):
    """De mogelijke types van een tijdelijke waterkerende constructie."""
    naam = 'KlTypeTWC'
    label = 'Type tijdelijke waterkerende constructie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlTypeTWC'
    definition = 'De mogelijke types van een tijdelijke waterkerende constructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTypeTWC'
    options = {
        'afsluitcaisson': KeuzelijstWaarde(invulwaarde='afsluitcaisson',
                                           label='afsluitcaisson',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeTWC/afsluitcaisson'),
        'droogzetkuip': KeuzelijstWaarde(invulwaarde='droogzetkuip',
                                         label='droogzetkuip',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeTWC/droogzetkuip'),
        'noodschot': KeuzelijstWaarde(invulwaarde='noodschot',
                                      label='noodschot',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeTWC/noodschot'),
        'schipdeur': KeuzelijstWaarde(invulwaarde='schipdeur',
                                      label='schipdeur',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeTWC/schipdeur'),
        'schotbalk': KeuzelijstWaarde(invulwaarde='schotbalk',
                                      label='schotbalk',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeTWC/schotbalk'),
        'taatskuip': KeuzelijstWaarde(invulwaarde='taatskuip',
                                      label='taatskuip',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTypeTWC/taatskuip')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

