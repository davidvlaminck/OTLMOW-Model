# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMIVMeetpuntAfmetingen(KeuzelijstField):
    """Lijst van standaardafmetingen van een lus van een MIV meetpunt."""
    naam = 'KlMIVMeetpuntAfmetingen'
    label = 'MIV meetpunt afmetingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlMIVMeetpuntAfmetingen'
    definition = 'Lijst van standaardafmetingen van een lus van een MIV meetpunt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMIVMeetpuntAfmetingen'
    options = {
        '1-5x1-8': KeuzelijstWaarde(invulwaarde='1-5x1-8',
                                    label='1.5x1.8',
                                    status='verwijderd',
                                    definitie='De afmeting 1.5x1.8 in meter (standaard afmeting).',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntAfmetingen/1-5x1-8'),
        '1-5x2-4': KeuzelijstWaarde(invulwaarde='1-5x2-4',
                                    label='1.5x2.4',
                                    status='verwijderd',
                                    definitie='De afmeting 1.5x2.4 in meter.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntAfmetingen/1-5x2-4'),
        '1-5x4': KeuzelijstWaarde(invulwaarde='1-5x4',
                                  label='1.5x4',
                                  status='verwijderd',
                                  definitie='De afmeting 1.5x4 in meter.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntAfmetingen/1-5x4'),
        'afwijkend': KeuzelijstWaarde(invulwaarde='afwijkend',
                                      label='Afwijkend',
                                      status='ingebruik',
                                      definitie='Alle afmetingen die niet standaard of breed zijn worden getypeerd als Afwijkend.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntAfmetingen/afwijkend'),
        'breed-1-5x2-4': KeuzelijstWaarde(invulwaarde='breed-1-5x2-4',
                                          label='Breed (1.5x2.4)',
                                          status='ingebruik',
                                          definitie='Breed (1.5x2.4)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntAfmetingen/breed-1-5x2-4'),
        'standaard-1-5x1-8': KeuzelijstWaarde(invulwaarde='standaard-1-5x1-8',
                                              label='Standaard (1.5x1.8)',
                                              status='ingebruik',
                                              definitie='Standaard (1.5x1.8)',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMIVMeetpuntAfmetingen/standaard-1-5x1-8')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

