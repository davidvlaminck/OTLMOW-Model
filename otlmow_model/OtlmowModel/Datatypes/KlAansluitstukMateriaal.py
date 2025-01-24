# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAansluitstukMateriaal(KeuzelijstField):
    """Het materiaal van het aansluitstuk."""
    naam = 'KlAansluitstukMateriaal'
    label = 'Aansluitstuk materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAansluitstukMateriaal'
    definition = 'Het materiaal van het aansluitstuk.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAansluitstukMateriaal'
    options = {
        'gres': KeuzelijstWaarde(invulwaarde='gres',
                                 label='gres',
                                 status='ingebruik',
                                 definitie='Gres',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/gres'),
        'koolstofstaal': KeuzelijstWaarde(invulwaarde='koolstofstaal',
                                          label='koolstofstaal',
                                          status='ingebruik',
                                          definitie='koolstofstaal',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/koolstofstaal'),
        'polyethyleen': KeuzelijstWaarde(invulwaarde='polyethyleen',
                                         label='polyethyleen',
                                         status='ingebruik',
                                         definitie='polyethyleen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/polyethyleen'),
        'pp': KeuzelijstWaarde(invulwaarde='pp',
                               label='pp',
                               status='ingebruik',
                               definitie='Polypropyleen',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/pp'),
        'pvc': KeuzelijstWaarde(invulwaarde='pvc',
                                label='pvc',
                                status='ingebruik',
                                definitie='Polyvinylchloride',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/pvc'),
        'pvc-u-composiet': KeuzelijstWaarde(invulwaarde='pvc-u-composiet',
                                            label='pvc-u-composiet',
                                            status='ingebruik',
                                            definitie='pvc-u-composiet',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/pvc-u-composiet'),
        'rvs': KeuzelijstWaarde(invulwaarde='rvs',
                                label='rvs',
                                status='ingebruik',
                                definitie='roestvrij staal',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/rvs'),
        'staal': KeuzelijstWaarde(invulwaarde='staal',
                                  label='staal',
                                  status='ingebruik',
                                  definitie='staal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAansluitstukMateriaal/staal')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

