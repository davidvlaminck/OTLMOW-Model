# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStopcontactAantalPolen(KeuzelijstField):
    """Mogelijke waarden voor het aantal polen van een stopcontact."""
    naam = 'KlStopcontactAantalPolen'
    label = 'stopcontact aantal polen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStopcontactAantalPolen'
    definition = 'Mogelijke waarden voor het aantal polen van een stopcontact.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStopcontactAantalPolen'
    options = {
        '3P': KeuzelijstWaarde(invulwaarde='3P',
                               label='3P',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStopcontactAantalPolen/3P'),
        '4P': KeuzelijstWaarde(invulwaarde='4P',
                               label='4P',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStopcontactAantalPolen/4P')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

