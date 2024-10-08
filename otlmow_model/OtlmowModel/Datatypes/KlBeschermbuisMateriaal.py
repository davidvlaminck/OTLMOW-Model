# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeschermbuisMateriaal(KeuzelijstField):
    """Keuzelijst voor het bepalen van het materiaal van de beschermbuis."""
    naam = 'KlBeschermbuisMateriaal'
    label = 'Beschermbuis materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermbuisMateriaal'
    definition = 'Keuzelijst voor het bepalen van het materiaal van de beschermbuis.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermbuisMateriaal'
    options = {
        'hdpe': KeuzelijstWaarde(invulwaarde='hdpe',
                                 label='HDPE',
                                 status='ingebruik',
                                 definitie='HDPE',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/hdpe'),
        'hdpe-pn10': KeuzelijstWaarde(invulwaarde='hdpe-pn10',
                                      label='HDPE PN10',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/hdpe-pn10'),
        'hdpe-sdr17': KeuzelijstWaarde(invulwaarde='hdpe-sdr17',
                                       label='HDPE SDR17',
                                       status='ingebruik',
                                       definitie='HDPE SDR17',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/hdpe-sdr17'),
        'opticalfiber': KeuzelijstWaarde(invulwaarde='opticalfiber',
                                         label='opticalFiber',
                                         status='ingebruik',
                                         definitie='opticalFiber',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/opticalfiber'),
        'pe': KeuzelijstWaarde(invulwaarde='pe',
                               label='PE',
                               status='ingebruik',
                               definitie='PE',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/pe'),
        'pvc': KeuzelijstWaarde(invulwaarde='pvc',
                                label='PVC',
                                status='ingebruik',
                                definitie='PVC',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/pvc'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='RVS',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermbuisMateriaal/rvs')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

