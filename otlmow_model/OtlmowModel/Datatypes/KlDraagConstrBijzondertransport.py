# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDraagConstrBijzondertransport(KeuzelijstField):
    """De mogelijkheden en manieren waarop een steun geschikt is om bijzonder transport mogelijk te maken."""
    naam = 'KlDraagConstrBijzondertransport'
    label = 'Draagconstructie bijzonder transport'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlDraagConstrBijzondertransport'
    definition = 'De mogelijkheden en manieren waarop een steun geschikt is om bijzonder transport mogelijk te maken.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraagConstrBijzondertransport'
    options = {
        'afkoppelbaar': KeuzelijstWaarde(invulwaarde='afkoppelbaar',
                                         label='afkoppelbaar',
                                         status='ingebruik',
                                         definitie='Het object is afkoppelbaar.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/afkoppelbaar'),
        'draaibaar': KeuzelijstWaarde(invulwaarde='draaibaar',
                                      label='draaibaar',
                                      status='ingebruik',
                                      definitie='Het object is draaibaar.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/draaibaar'),
        'geen-voorziening': KeuzelijstWaarde(invulwaarde='geen-voorziening',
                                             label='geen voorziening',
                                             status='ingebruik',
                                             definitie='Geen voorziening.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/geen-voorziening'),
        'kantelbaar': KeuzelijstWaarde(invulwaarde='kantelbaar',
                                       label='kantelbaar',
                                       status='ingebruik',
                                       definitie='Het object is kantelbaar.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBijzondertransport/kantelbaar')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

