# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGraadVanStatischeBepaaldheid(KeuzelijstField):
    """De statische bepaaldheid van het brugdeel."""
    naam = 'KlGraadVanStatischeBepaaldheid'
    label = 'Graad van statische bepaaldheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlGraadVanStatischeBepaaldheid'
    definition = 'De statische bepaaldheid van het brugdeel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGraadVanStatischeBepaaldheid'
    options = {
        'hyperstatisch': KeuzelijstWaarde(invulwaarde='hyperstatisch',
                                          label='Hyperstatisch',
                                          status='ingebruik',
                                          definitie='Statisch onbepaald. De reacties (de momenten en dwarskrachten) kunnen niet worden berekend met de statica alleen.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGraadVanStatischeBepaaldheid/hyperstatisch'),
        'isostatisch': KeuzelijstWaarde(invulwaarde='isostatisch',
                                        label='Isostatisch',
                                        status='ingebruik',
                                        definitie='Statisch bepaald. De reacties en inwendige krachten zijn te berekenen met de statica.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGraadVanStatischeBepaaldheid/isostatisch')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

