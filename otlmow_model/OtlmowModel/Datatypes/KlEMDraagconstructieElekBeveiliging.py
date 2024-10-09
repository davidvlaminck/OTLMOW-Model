# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEMDraagconstructieElekBeveiliging(KeuzelijstField):
    """Type elektrische beveiliging aanwezig in de draagconstructie."""
    naam = 'KlEMDraagconstructieElekBeveiliging'
    label = 'EM-draagconstructie elektrische beveiliging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlEMDraagconstructieElekBeveiliging'
    definition = 'Type elektrische beveiliging aanwezig in de draagconstructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEMDraagconstructieElekBeveiliging'
    options = {
        'automaat': KeuzelijstWaarde(invulwaarde='automaat',
                                     label='automaat',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/automaat'),
        'automaat-varistor': KeuzelijstWaarde(invulwaarde='automaat-varistor',
                                              label='automaat + varistor',
                                              status='ingebruik',
                                              definitie='automaat + varistor',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/automaat-varistor'),
        'differentieelautomaat': KeuzelijstWaarde(invulwaarde='differentieelautomaat',
                                                  label='differentieelautomaat',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/differentieelautomaat'),
        'differentieelautomaat-varistor': KeuzelijstWaarde(invulwaarde='differentieelautomaat-varistor',
                                                           label='differentieelautomaat + varistor',
                                                           status='ingebruik',
                                                           definitie='differentieelautomaat + varistor',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/differentieelautomaat-varistor'),
        'smeltzekering': KeuzelijstWaarde(invulwaarde='smeltzekering',
                                          label='smeltzekering',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/smeltzekering')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

