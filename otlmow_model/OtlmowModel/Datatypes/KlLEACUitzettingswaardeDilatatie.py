# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACUitzettingswaardeDilatatie(KeuzelijstField):
    """De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing."""
    naam = 'KlLEACUitzettingswaardeDilatatie'
    label = 'Uitzetttingswaarde dilatatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACUitzettingswaardeDilatatie'
    definition = 'De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACUitzettingswaardeDilatatie'
    options = {
        '10-cm': KeuzelijstWaarde(invulwaarde='10-cm',
                                  label='10 cm',
                                  status='ingebruik',
                                  definitie='De uitzettingswaarde is 10 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACUitzettingswaardeDilatatie/10-cm'),
        '20-cm': KeuzelijstWaarde(invulwaarde='20-cm',
                                  label='20 cm',
                                  status='ingebruik',
                                  definitie='De uitzettingswaarde is 20 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACUitzettingswaardeDilatatie/20-cm'),
        '90-cm': KeuzelijstWaarde(invulwaarde='90-cm',
                                  label='90 cm',
                                  status='ingebruik',
                                  definitie='De uitzettingswaarde is 90 cm.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACUitzettingswaardeDilatatie/90-cm')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

