# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriLusFunctie(KeuzelijstField):
    """Keuzelijst met verschillende types detectielussen naar functie."""
    naam = 'KlVriLusFunctie'
    label = 'VRI-lus functie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVriLusFunctie'
    definition = 'Keuzelijst met verschillende types detectielussen naar functie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriLusFunctie'
    options = {
        'KAR-inmeldlus': KeuzelijstWaarde(invulwaarde='KAR-inmeldlus',
                                          label='KAR inmeldlus',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/KAR-inmeldlus'),
        'KAR-uitmeldlus': KeuzelijstWaarde(invulwaarde='KAR-uitmeldlus',
                                           label='KAR uitmeldlus',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/KAR-uitmeldlus'),
        'afstandslus': KeuzelijstWaarde(invulwaarde='afstandslus',
                                        label='afstandslus',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/afstandslus'),
        'filelus': KeuzelijstWaarde(invulwaarde='filelus',
                                    label='filelus',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/filelus'),
        'hiaatlus': KeuzelijstWaarde(invulwaarde='hiaatlus',
                                     label='hiaatlus',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/hiaatlus'),
        'stopstreeplus': KeuzelijstWaarde(invulwaarde='stopstreeplus',
                                          label='stopstreeplus',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/stopstreeplus'),
        'tellus': KeuzelijstWaarde(invulwaarde='tellus',
                                   label='tellus',
                                   status='ingebruik',
                                   definitie='tellus',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusFunctie/tellus')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

