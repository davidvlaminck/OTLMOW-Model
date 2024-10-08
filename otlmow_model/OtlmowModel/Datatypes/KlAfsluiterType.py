# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAfsluiterType(KeuzelijstField):
    """De types van de afsluiter."""
    naam = 'KlAfsluiterType'
    label = 'Afsluiter type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfsluiterType'
    definition = 'De types van de afsluiter.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfsluiterType'
    options = {
        'steekschuif': KeuzelijstWaarde(invulwaarde='steekschuif',
                                        label='steekschuif',
                                        status='ingebruik',
                                        definitie='De steekschuif is een verticaal bewegend afsluitorgaan, en kan rond, vierkant of rechthoekig zijn.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluiterType/steekschuif'),
        'wandafsluiter': KeuzelijstWaarde(invulwaarde='wandafsluiter',
                                          label='wandafsluiter',
                                          status='ingebruik',
                                          definitie='Een afsluiter voor de beheersing van water',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluiterType/wandafsluiter')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

