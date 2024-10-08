# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDraagstructuurBWCTWC(KeuzelijstField):
    """Type van draagstructuur gebruikt in beweegbare waterkerende constructies en tijdelijke waterkerende constructies."""
    naam = 'KlDraagstructuurBWCTWC'
    label = 'Draagstructuur BWCTWC'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlDraagstructuurBWCTWC'
    definition = 'Type van draagstructuur gebruikt in beweegbare waterkerende constructies en tijdelijke waterkerende constructies.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraagstructuurBWCTWC'
    options = {
        'achterhar': KeuzelijstWaarde(invulwaarde='achterhar',
                                      label='achterhar',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagstructuurBWCTWC/achterhar'),
        'beplating': KeuzelijstWaarde(invulwaarde='beplating',
                                      label='beplating',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagstructuurBWCTWC/beplating'),
        'bovenregel': KeuzelijstWaarde(invulwaarde='bovenregel',
                                       label='bovenregel',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagstructuurBWCTWC/bovenregel'),
        'diagonaal': KeuzelijstWaarde(invulwaarde='diagonaal',
                                      label='diagonaal',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagstructuurBWCTWC/diagonaal'),
        'onderregel': KeuzelijstWaarde(invulwaarde='onderregel',
                                       label='onderregel',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagstructuurBWCTWC/onderregel'),
        'tussenregel': KeuzelijstWaarde(invulwaarde='tussenregel',
                                        label='tussenregel',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagstructuurBWCTWC/tussenregel'),
        'tussenstijl': KeuzelijstWaarde(invulwaarde='tussenstijl',
                                        label='tussenstijl',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagstructuurBWCTWC/tussenstijl'),
        'voorhar': KeuzelijstWaarde(invulwaarde='voorhar',
                                    label='voorhar',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagstructuurBWCTWC/voorhar')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

