# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGraadVanBeweegbaarheid(KeuzelijstField):
    """Op welke manier het brugdeel kan bewegen."""
    naam = 'KlGraadVanBeweegbaarheid'
    label = 'graad van beweegbaarheid'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlGraadVanBeweegbaarheid'
    definition = 'Op welke manier het brugdeel kan bewegen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGraadVanBeweegbaarheid'
    options = {
        'beweegbaar': KeuzelijstWaarde(invulwaarde='beweegbaar',
                                       label='Beweegbaar',
                                       status='ingebruik',
                                       definitie='Het brugdeel is beweegbaar.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGraadVanBeweegbaarheid/beweegbaar'),
        'vast': KeuzelijstWaarde(invulwaarde='vast',
                                 label='Vast',
                                 status='ingebruik',
                                 definitie='Het brugdeel is vast en beweegt niet.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGraadVanBeweegbaarheid/vast')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

